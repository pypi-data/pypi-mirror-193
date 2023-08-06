"""求结构距离

用法：
1. # 命令行直接使用
    $ python3 dist.py <structure1.as> <structure2.as> 

2. # 写在python脚本中
    from dist import get_distance

    spo1, ele1, lat1 = get_spo_ele_lat(structure1)
    spo2, ele2, lat2 = get_spo_ele_lat(structure2)
    distance = get_distance(spo1, spo2, lat1, lat2)
"""

from neb_utils import get_spo_ele_lat
import numpy as np
np.set_printoptions(suppress=True)  # 不使用科学计数法


def set_pbc(spo: np.ndarray or list):
    """根据周期性边界条件将分数坐标分量移入 [-0.5, 0.5) 区间

    Parameters
    ----------
    spo (np.ndarray or list): 分数坐标列表

    Returns
    -------
    np.ndarray:
        符合周期性边界条件的分数坐标列表
    """
    # 周期性边界条件
    pbc_spo = []  # pbc scaled_positions, Natom x 3
    for xyz in spo:
        pbc_s = []  # pbc scaled_position, 3
        for f in xyz:
            if f < -0.5:
                f += 1
            elif f >= 0.5:
                f -= 1
            pbc_s.append(f)
        pbc_spo.append(pbc_s)
    
    return np.array(pbc_spo)


def get_distance(spo1: np.ndarray, spo2: np.ndarray, lat1: np.ndarray, lat2: np.ndarray):
    """根据两个结构的分数坐标和晶胞计算距离

    Parameters
    ----------
    spo1 : np.ndarray
        分数坐标1
    spo2 : np.ndarray
        分数坐标2
    lat1 : np.ndarray
        晶胞1
    lat2 : np.ndarray
        晶胞2

    Returns
    -------
    float
        距离
    """
    diff_spo = spo1 - spo2  # 分数坐标差
    avglatv = 0.5*(lat1 + lat2)  # 平均晶格矢量
    pbc_diff_spo = set_pbc(diff_spo)  # 笛卡尔坐标差
    # 分数坐标点乘平均晶胞，转回笛卡尔坐标
    pbc_diff_pos = np.dot(pbc_diff_spo, avglatv)  # 笛卡尔坐标差
    distance = np.sqrt(np.sum(pbc_diff_pos**2))

    return distance


if __name__ == '__main__':
    import sys
    assert len(sys.argv) == 3, 'Usage: python3 dist.py <structure1.as> <structure2.as>'
    structure1 = sys.argv[1]
    structure2 = sys.argv[2]

    spo1, ele1, lat1 = get_spo_ele_lat(structure1)
    spo2, ele2, lat2 = get_spo_ele_lat(structure2)
    distance = get_distance(spo1, spo2, lat1, lat2)

    print('--> dist:', distance)
