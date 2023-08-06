"""h5 -> neb_movie.json 从而可以用DeviceStudio打开观察多个结构构成的轨迹动图

功能：

1. 允许用户指定离子步编号（第几个loop），读取此时的00，01，...，中的结构和能量信息
2. 初始插值结构预览：从structure00.as，structure01.as，...，中读取结构信息
"""

import os
import h5py
import json
import numpy as np
from neb_utils import get_neb_subfolders, get_pos_ele_lat, get_ele_from_h5


def h5_to_neb_movie_json(directory: str = os.getcwd(), loop: int = 0, output: str = None):
    """从NEB路径下的h5文件读取指定loop数的结构和能量信息，写入json文件，以便用DeviceStudio打开观察

    Parameters
    ----------
    directory : str
        NEB路径，默认当前路径
    loop : str
        loop数，默认0，初始插值构型
    output : str
        生成的json文件名, 默认'neb_movie_n.json'，n是loop数
    """

    if output is None:
        output = 'neb_movie_{}.json'.format(loop)

    # ^ 读取前，准备好json文件所需数组框架
    subfolders = get_neb_subfolders(directory)
    nimage = len(subfolders)

    '''Distance group
    ReactionCoordinate (nimage x 1)
    '''
    reactionCoordinates = np.zeros(shape=nimage)  # optional

    '''Energy group
    TotalEnergy (nimage x 1)
    '''
    totalEnergies = np.zeros(shape=nimage)  # optional

    '''Force group
    MaxForce/Tangent (nimage-2 x 1)
    '''
    maxForces = np.zeros(shape=nimage-2)  # optional
    tangents = np.zeros(shape=nimage-2)  # optional

    '''Iteration group
    01(img) > 0(loop) > MaxForce/TotalEnergy
    '''
    MaxForces = np.zeros(shape=(nimage-2, loop+1))  # optional
    TotalEnergies = np.zeros(shape=(nimage-2, loop+1))  # optional

    '''Relaxed/Unrelaxed Structure group
    0(img) > Atoms > 0(atom) > Element(str)/Fix([])/Mag([])/Position(3x1)/Pot([])
    0(img) > CoordinateType == 'Cartesian' or 'Direct'
    0(img) > Lattice(9x1)
    '''
    Poses = []  # nimage x Natom x 3 , read
    Elems = []  # nimage x Natom, read
    Latvs = []  # nimage x 9, read
    coordinateTypes = ['Cartesian'] * nimage  # set
    Fixs = []  # nimage x Natom x 3, set

    # ^ 判断需要使用哪个功能
    flag = 0
    for folder in subfolders:
        '''如果是首尾两个构型，最多只有scf.h5文件，没有neb.h5文件
        用户如果算NEB的时候，不计算首尾构型的自洽，
         或者在别处算完了但是没有复制到首尾文件夹中并命名为scf.h5，
          便不能使用第一个功能
        '''
        if folder == subfolders[0] or folder == subfolders[-1]:
            h5_path = os.path.join(directory, folder, 'scf.h5')
        else:
            h5_path = os.path.join(directory, folder, f'neb{folder}.h5')

        if os.path.exists(h5_path):
            flag = 1  # 第一个功能
        else:
            structure_path = os.path.join(
                directory, folder, f'structure{folder}.as')
            if not os.path.exists(structure_path):
                raise FileNotFoundError(
                    f'{h5_path}中，neb{folder}.h5和structure{folder}.as文件都不存在！')
            else:
                flag = 2  # 第二个功能

    # ^ 开始分功能读取数据
    if flag == 1:  # read from h5 file
        print('读取h5文件中的结构和能量信息...')
        for i, folder in enumerate(subfolders):
            if folder == subfolders[0] or folder == subfolders[-1]:
                h5_path = os.path.join(directory, folder, 'scf.h5')
                data = h5py.File(h5_path)
                # 不影响可视化，直接定为0
                if folder == subfolders[0]:
                    reactionCoordinates[i] = 0

            else:
                h5_path = os.path.join(directory, folder, f'neb{folder}.h5')
                data = h5py.File(h5_path)
                # reading...
                reactionCoordinates[i-1] = np.array(
                    data.get('/ReactionCoordinate'))[-2]
                maxForces[i-1] = np.array(data.get('/MaxForce'))[-1]
                tangents[i-1] = np.array(data.get('/Tangent'))[-1]
                if folder == subfolders[-2]:
                    reactionCoordinates[i +
                                        1] = np.array(data.get('/ReactionCoordinate'))[-1]
                # read MaxForces and TotalEnergies
                nionStep = np.array(data.get('/MaxForce')).shape[0]
                assert loop <= nionStep, f'总共只完成了{nionStep}个离子步!'
                for j in range(loop):
                    MaxForces[i-1, j+1] = np.array(data.get('/MaxForce'))[j]
                    TotalEnergies[i-1, j +
                                  1] = np.array(data.get('/TotalEnergy'))[j]

            totalEnergies[i] = np.array(data.get('/Energy/TotalEnergy0'))
            pos = np.array(data.get('/AtomInfo/Position'))
            Poses.append(pos)

            elems = get_ele_from_h5(hpath=h5_path)
            Elems.append(elems)

            lat = np.array(data.get('/AtomInfo/Lattice'))
            Latvs.append(lat)

            fix_array = np.array(data.get('/AtomInfo/Fix'))
            for fix in fix_array:
                if fix == 0.0:
                    F = False
                elif fix == 1.0:
                    F = True
                else:
                    raise ValueError('Fix值只能为0或1')
                Fixs.append(F)

        Natom = len(Elems[0])

        # 累加reactionCoordinates中的元素
        for i in range(1, len(reactionCoordinates)):
            reactionCoordinates[i] += reactionCoordinates[i-1]

    elif flag == 2:  # read from structure.as file
        print('读取初始插值结构以生成NEB_movie.json文件...')
        for i, folder in enumerate(subfolders):
            structure_path = os.path.join(
                directory, folder, f'structure{folder}.as')
            pos, ele, lat = get_pos_ele_lat(structure_path)
            Poses.append(pos)
            Elems.append(ele)
            Latvs.append(lat)
        
        Natom = len(Elems[0])

    # reshape data
    Poses = np.array(Poses).reshape((nimage,Natom,3))
    Elems = np.array(Elems).reshape((nimage,Natom))
    Latvs = np.array(Latvs).reshape((nimage,9))

    # ^ 将数据按特定格式构造成字典
    IterDict = {}
    for s, sf in enumerate(subfolders):
        if sf == subfolders[0] or sf == subfolders[-1]:
            continue
        else:
            Eflist = []
            for l in range(loop+1):
                ef = {'MaxForce': MaxForces[s-1, l].tolist(),
                      'TotalEnergy': TotalEnergies[s-1, l].tolist()}
                Eflist.append(ef)
                iterDict = {sf: Eflist}  # construct sub-dict
                IterDict.update(iterDict)  # append sub-dict

    RSList = []
    '''
    从外到内依次遍历 构型、原子（子字典）
    原子的键值对为：'Atoms': 原子信息列表
    原子信息列表是一个由字典组成的列表，每个字典对应一个原子的信息
    '''
    for s, sf in enumerate(subfolders):
        pos = Poses[s]
        lat = Latvs[s]
        elem = Elems[s]
        atoms = []
        for i in range(len(elem)):
            atom = {'Element': elem[i],
                    'Fix': Fixs[i*3:i*3+3],
                    'Mag': [],  # empty
                    'Position': pos[i].tolist(),
                    'Pot': ""}  # empty
            atoms.append(atom)
        rs = {'Atoms': atoms,
              'CoordinateType': coordinateTypes[s],
              'Lattice': lat.tolist()}
        RSList.append(rs)

    URSList = []  # DS似乎并不读取这部分信息，空置即可

    data = {'Distance': {'ReactionCoordinate': reactionCoordinates.tolist()},
            'Energy': {'TotalEnergy': totalEnergies.tolist()},
            'Force': {'MaxForce': maxForces.tolist(),
                      'Tangent': tangents.tolist()},
            'Iteration': IterDict,
            'RelaxedStructure': RSList,
            'UnrelaxedStructure': URSList}

    # ^ 将字典写入json文件
    with open(output, 'w') as f:
        json.dump(data, f, indent=4)


if __name__ == '__main__':
    import sys
    if len(sys.argv) == 1:
        h5_to_neb_movie_json()
    elif len(sys.argv) == 4:
        h5_to_neb_movie_json(sys.argv[1], int(sys.argv[2]), sys.argv[3])
    else:
        print('=================== 生成轨迹动图 ==========================')
        print(
            'Usage: python h5_to_neb_movie_json.py [directory] [loop] [output]')
        print('directory: NEB路径，默认当前路径')
        print('loop: NEB计算的第几个离子步，对应日志中的loop数，默认0，即插值结构')
        print('output: 输出的json文件名，默认neb_movie_${loop}.json')
        print('==========================================================\n')
        raise ValueError('参数输入错误')
