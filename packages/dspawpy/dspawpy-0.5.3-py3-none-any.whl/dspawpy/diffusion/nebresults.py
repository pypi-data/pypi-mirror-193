from neb_utils import get_neb_subfolders
import matplotlib.pyplot as plt
from nebef import getef
from neb_utils import plot_neb_converge
import os
from nebef import getef, printef
from scipy.interpolate import interp1d
import numpy as np

intro = """NEB任务完成总结
!!! 如果neb.iniFin = false，请将初末态的自洽结果移入对应子文件夹
将依次执行以下步骤：
1. 绘制能垒图
2. 打印各构型受力、反应坐标、能量、与初始构型的能量差
3. 绘制并保存结构优化过程的能量和受力收敛过程图

用法：
1. 命令行下运行
    $ python nebresults.py [NEB路径]
2. 在python中导入
    from nebresults import summary
    summary(directory) # 默认当前路径
"""


def summary(directory: str = os.getcwd()):
    """NEB任务完成总结
    依次执行以下步骤：
    1. 绘制能垒图
    2. 打印各构型受力、反应坐标、能量、与初始构型的能量差
    3. 绘制并保存结构优化过程的能量和受力收敛过程图

    Parameters
    ----------
    directory : str, 可选
        NEB路径, 默认当前路径
    ! 若inifin=false，用户必须将自洽的scf.h5或system.json放到初末态子文件夹中
    """
    # 1. 绘制能垒图
    print('--> 1. 绘制能垒图...')
    # TODO 考虑重写plot_neb_barrier
    subfolders, resort_mfs, rcs, ens, dEs = getef(directory)
    inter_f = interp1d(rcs, dEs, kind="cubic")
    xnew = np.linspace(rcs[0], rcs[-1], 100)
    ynew = inter_f(xnew)
    plt.plot(xnew, ynew, c="b")
    plt.scatter(rcs, dEs, c="r")
    plt.xlabel("Reaction Coordinate")
    plt.ylabel("Energy")
    plt.savefig(f"{directory}/neb_reaction_coordinate.png")

    # 2. 打印各构型受力、反应坐标、能量、与初始构型的能量差
    print('\n--> 2. 打印NEB计算时各构型的能量和受力...')
    printef(directory)

    # 3. 绘制并保存结构优化过程的能量和受力收敛过程图到各构型文件夹中
    print('\n--> 3. 绘制收敛过程图到各构型文件夹中...')
    subfolders = get_neb_subfolders(directory)
    for subfolder in subfolders[1:len(subfolders)-1]:
        print(f"----> {subfolder}/converge.png...")
        plot_neb_converge(neb_dir=directory, image_key=subfolder)
        plt.savefig(f"{directory}/{subfolder}/converge.png")
    print('\n完成!')


if __name__ == '__main__':
    import sys
    if len(sys.argv) == 1:
        summary()
    elif len(sys.argv) == 2:
        summary(sys.argv[1])
    else:
        print('='*50)
        print(intro)
        print('='*50)
        sys.exit(1)
