"""对屏幕输出计算信息

用法：
1. 命令行使用
    $ python3 nebef.py [neb_directory] 
2. 写在python脚本中
    from nebef import print_ef
    print_ef(neb_directory)
"""

import h5py
import json
import numpy as np
import os


def getef(directory: str = os.getcwd()):
    """从dire路径读取NEB计算时各构型的能量和受力

    input:
        - directory: NEB计算的路径，默认当前路径
    output:
        - subfolders: 构型文件夹名
        - resort_mfs: 构型受力的最大分量 
        - rcs: 反应坐标
        - ens: 电子总能
        - dE: 与初始构型的能量差
    """

    from neb_utils import get_neb_subfolders
    subfolders = get_neb_subfolders(directory)
    Nimage = len(subfolders)

    ens = []
    dEs = np.zeros(Nimage)
    rcs = [0]
    mfs = []

    # read energies
    count = 1
    for i, subfolder in enumerate(subfolders):
        if i == 0 or i == Nimage-1:
            jsf = os.path.join(directory, subfolder, f'system{subfolder}.json')
            hf = os.path.join(directory, subfolder, 'scf.h5')
            if os.path.exists(jsf):
                with open(jsf, 'r') as f:
                    data = json.load(f)
                en = data['Energy']['TotalEnergy0']
                if i == 0 or i == Nimage-1:
                    mf = np.max(np.abs(data['Force']['ForceOnAtoms']))
                    mfs.append(mf)
            elif os.path.exists(hf):
                data = h5py.File(hf)
                en = np.array(data.get('/Energy/TotalEnergy0'))
                if i == 0 or i == Nimage-1:
                    mf = np.max(
                        np.abs(np.array(data.get('/Force/ForceOnAtoms'))))
                    mfs.append(mf)
            else:
                raise FileNotFoundError(
                    '无法找到记录构型%s的能量和受力的system.json或scf.h5文件' % subfolder)
            ens.append(en)

        else:
            jsf = os.path.join(directory, subfolder, f'neb{subfolder}.json')
            hf = os.path.join(directory, subfolder, f'neb{subfolder}.h5')

            if os.path.exists(jsf):
                with open(jsf, 'r') as f:
                    data = json.load(f)
                Nion_step = len(data)
                en = data[Nion_step-1]['TotalEnergy']
                mf = data[Nion_step-1]['MaxForce']  # 最后一步的最大受力
                rc = data[Nion_step-1]['ReactionCoordinate'][0]  # 最后一步的反应坐标
                rcs.append(rc)
                if count == Nimage-2:  # before final image
                    rc = data[Nion_step-1]['ReactionCoordinate'][1]  # 最后一步的反应坐标
                    rcs.append(rc)
            elif os.path.exists(hf):
                data = h5py.File(hf)
                en = np.array(data.get('/Energy/TotalEnergy0'))
                mf = np.array(data.get('/MaxForce'))[-1]
                rc = np.array(data.get('/ReactionCoordinate'))[-2]
                rcs.append(rc)
                if count == Nimage-2:  # before final image
                    rc = np.array(data.get('/ReactionCoordinate'))[-1]
                    rcs.append(rc)
            else:
                raise FileNotFoundError('无法找到neb%s.json或hdf5文件' % subfolder)

            ens.append(en)
            mfs.append(mf)

            # get dE
            dE = ens[count] - ens[0]
            dEs[i] = dE
            count += 1
    dEs[-1] = ens[Nimage-1] - ens[0]

    # rcs 改成累加值
    for i in range(1, len(rcs)):
        rcs[i] += rcs[i-1]

    rcs = np.array(rcs)

    resort_mfs = [mfs[0]]
    final_mf = mfs[1]
    for j in range(2, len(mfs)):
        resort_mfs.append(mfs[j])
    resort_mfs.append(final_mf)

    return subfolders, resort_mfs, rcs, ens, dEs


def printef(directory):
    """打印NEB计算时各构型的能量和受力
    """
    subfolders, resort_mfs, rcs, ens, dEs = getef(directory)
    # printout summary
    print('构型\t受力(eV/Å)\t反应坐标(Å)\t此构型的能量(eV)\t与初始构型的能量差(eV)')
    for i in range(len(subfolders)):  # 注意格式化输出，对齐
        print('%s\t%8.4f\t%8.4f\t%12.4f\t%20.4f' %
              (subfolders[i], resort_mfs[i], rcs[i], ens[i], dEs[i]))


if __name__ == '__main__':
    import sys
    assert len(sys.argv) <= 2, 'Usage: python3 dist.py [neb_directory]'
    if len(sys.argv) == 1:
        dire = os.getcwd()
    else:
        dire = sys.argv[1]
    printef(dire)
