"""NEB系列一些工具函数，包括
1. get_neb_subfolders: 获取NEB子文件夹名称列表
2. get_spo_ele_lat: 从结构文件中读取分数坐标、元素列表，和晶胞矩阵
3. get_pos_ele_lat: 从结构文件中读取分数坐标、元素列表，和晶胞矩阵

用法：
    在python中导入这里的函数，比如：
    from neb_utils import get_neb_subfolders
"""

import os
import numpy as np


def get_neb_subfolders(directory: str = os.getcwd()):
    """获取NEB子文件夹名称列表
    将directory路径下的子文件夹名称列表按照数字大小排序
    仅保留形如00，01数字类型的NEB子文件夹路径

    Parameters
    ----------
    subfolders : list
        子文件夹名称列表

    Returns
    -------
    list
        排序后的子文件夹名称列表
    """
    raw_subfolders = next(os.walk(directory))[1]
    subfolders = []
    for subfolder in raw_subfolders:
        try:
            assert 0 <= int(subfolder) < 100
            subfolders.append(subfolder)
        except:
            pass
    subfolders.sort()  # 从小到大排序
    return subfolders


def get_spo_ele_lat(spath: str):
    """从结构文件中读取分数坐标、元素列表，和晶胞信息

    input:
        - spath: 结构文件路径

    output:
        - spos: 分数坐标分量数组，Natom x 3
        - ele: 元素列表, Natom x 1
        - latv: 晶胞矢量数组，3 x 3
    """

    with open(spath, 'r') as f:
        lines = f.readlines()
        Natom = int(lines[1])  # 原子总数
        ele = [line.split()[0] for line in lines[7:7+Natom]]  # 元素列表

        # 晶格矢量
        latv = np.array([line.split()
                         for line in lines[3:6]], dtype=float)
        # xyz坐标分量
        coord = np.array([line.split()[1:4]
                          for line in lines[7:7+Natom]], dtype=float)
        if lines[6].startswith('C'):  # 笛卡尔 --> 分数坐标
            spos = np.linalg.solve(latv.T, np.transpose(coord)).T
        elif lines[6].startswith('D'):
            spos = coord
        else:
            raise ValueError(f'{spath}中的坐标类型未知！')

    return spos, ele, latv


def get_pos_ele_lat(spath: str):
    """从结构文件中读取坐标、元素列表，和晶胞信息

    input:
        - spath: 结构文件路径

    output:
        - pos: 坐标分量数组，Natom x 3
        - ele: 元素列表, Natom x 1
        - latv: 晶胞矢量数组，3 x 3
    """

    with open(spath, 'r') as f:
        lines = f.readlines()
        Natom = int(lines[1])  # 原子总数
        ele = [line.split()[0] for line in lines[7:7+Natom]]  # 元素列表

        # 晶格矢量
        latv = np.array([line.split()
                         for line in lines[3:6]], dtype=float)
        # xyz坐标分量
        coord = np.array([line.split()[1:4]
                          for line in lines[7:7+Natom]], dtype=float)
        if lines[6].startswith('C'):
            pos = coord
        elif lines[6].startswith('D'):  # 分数 --> 笛卡尔
            pos = np.dot(coord, latv)
        else:
            raise ValueError(f'{spath}中的坐标类型未知！')

    return pos, ele, latv


def get_ele_from_h5(hpath: str = 'aimd.h5'):
    """从h5文件中读取元素列表
    """
    import h5py
    data = h5py.File(hpath)
    Elements_bytes = np.array(data.get('/AtomInfo/Elements'))
    tempdata = np.array([i.decode() for i in Elements_bytes])
    ele = ''.join(tempdata).split(';')

    return ele


def get_coordinateType_from_h5(hpath: str = 'aimd.h5'):
    """从h5文件中读取坐标类型
    """
    import h5py
    data = h5py.File(hpath)
    CoordinateType = np.array(data.get('/AtomInfo/CoordinateType'))
    tempdata = np.array([i.decode() for i in CoordinateType])
    ct = ''.join(tempdata).split(';')

    return ct


def plot_neb_converge(neb_dir: str, image_key="01"):
    """

    Args:
        neb_dir: neb.h5 directory
        image_key: image key 01,02,03...

    Returns:
            subplot left ax,right ax
    """
    if os.path.exists(f"{neb_dir}/neb.h5"):
        import h5py
        neb_total = h5py.File(f"{neb_dir}/neb.h5")
        maxforce = np.array(neb_total.get(
            "/Iteration/" + image_key + "/MaxForce"))
        total_energy = np.array(
            neb_total.get("/Iteration/" + image_key + "/TotalEnergy"))

    elif os.path.exists(f"{neb_dir}/neb.json"):
        import json
        with open(f"{neb_dir}/neb.json", 'r') as fin:
            neb_total = json.load(fin)
        neb = neb_total["Iteration"][image_key]
        maxforce = []
        total_energy = []
        for n in neb:
            maxforce.append(n["MaxForce"])
            total_energy.append(n["TotalEnergy"])

        maxforce = np.array(maxforce)
        total_energy = np.array(total_energy)

    else:
        print(f"{neb_dir}路径中找不到neb.h5或者neb.json文件")

    x = np.arange(len(maxforce))

    force = maxforce
    energy = total_energy

    import matplotlib.pyplot as plt
    fig = plt.figure()
    ax1 = fig.add_subplot(111)

    ax1.plot(x, force, label="Max Force", c="black")
    ax1.set_xlabel("Number of ionic step")
    ax1.set_ylabel("Force (eV/Å)")

    ax2 = ax1.twinx()
    ax2.plot(x, energy, label="Energy", c="r")
    ax2.set_xlabel("Number of ionic step")
    ax2.set_ylabel("Energy (eV)")
    ax2.ticklabel_format(useOffset=False)  # y轴坐标显示绝对值而不是相对值

    fig.legend(loc=1, bbox_to_anchor=(1, 1), bbox_transform=ax1.transAxes)
    plt.tight_layout()

    return ax1, ax2
