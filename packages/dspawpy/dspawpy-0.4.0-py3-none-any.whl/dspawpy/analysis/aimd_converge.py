'''
监控并绘制AIMD总能、动能、压力、应力、温度变化过程  
'''
import matplotlib.pyplot as plt
import numpy as np
import h5py


def read_data(h5file, index: str = None):
    '''
    从h5file指定的路径读取h5文件所需的数据
    '''
    hf = h5py.File(h5file)  # 加载h5文件
    Nstep = len(np.array(hf.get('/Structures')))-2  # 步数（可能存在未完成的）
    ys = np.empty(Nstep)  # 准备一个空数组

    # 开始读取
    if index == '5':
        for i in range(1, Nstep+1):
            ys[i-1] = np.linalg.det(hf.get('/Structures/Step-%d/Lattice' % i))
    else:
        map = {'1': 'IonsKineticEnergy',
               '2': 'TotalEnergy0',
               '3': 'PressureKinetic',
               '4': 'Temperature'}
        for i in range(1, Nstep+1):
            # 如果计算中断，则没有PressureKinetic这个键
            try:
                ys[i-1] = np.array(hf.get('/AimdInfo/Step-%d/%s' % (i, map[index])))
            except:
                ys[i-1] = 0
                ys = np.delete(ys, -1)
                print(f'-> 计算中断于第{Nstep}步，未读取到该步的压力数据！')

    Nstep = len(ys) # 步数更新为实际完成的步数

    # 返回xs，ys两个数组
    return np.linspace(1, Nstep, Nstep), np.array(ys)


def plot_aimd(h5file: str = 'aimd.h5', show: bool = False):
    '''
    根据用户指定的h5文件画图，
    如果show为真则展示交互界面，否则直接保存图片为 aimd.png
    '''
    # 读取用户输入
    flag_str = input(
        '请选择需要观察的数据编号（用空格隔开）：1.动能 2.总能 3.压力 4.温度 5.体积；\n直接回车，则全部绘制\n==> ')
    flags_str = flag_str.strip().split()
    # 处理用户输入，按顺序去重
    temp = set()
    flags = [x for x in flags_str if x not in temp and (temp.add(x) or True)]
    for flag in flags:
        assert flag in ['1', '2', '3', '4', '5'], "输入错误！"

    if not flags:
        flags = ['1', '2', '3', '4', '5']

    # 开始画组合图
    N_figs = len(flags)
    fig, axes = plt.subplots(N_figs, 1, sharex=True, figsize=(6, 2*N_figs))
    if N_figs == 1:  # 'AxesSubplot' object is not subscriptable
        axes = [axes]  # 避免上述类型错误
    fig.suptitle('DSPAW AIMD')
    for i, flag in enumerate(flags):
        print('正在处理子图'+flag)
        # 读取数据
        xs, ys = read_data(h5file, flag)
        axes[i].plot(xs, ys)  # 绘制坐标点
        # 子图的y轴标签
        if flag == '1':
            axes[i].set_ylabel('Kinetic Energy (eV)')
        elif flag == '2':
            axes[i].set_ylabel('Energy (eV)')
        elif flag == '3':
            axes[i].set_ylabel('Pressure Kinetic (kbar)')
        elif flag == '4':
            axes[i].set_ylabel('Temperature (K)')
        else:
            axes[i].set_ylabel('Volume (Angstrom^3)')

    fig.tight_layout()
    if show:
        plt.show()
    plt.savefig('aimd.png')
    print('--> 图片已保存为 aimd.png')


if __name__ == "__main__":
    '''用户可以这么写自己的脚本：
    from dspawpy.analysis.aimd import plot_aimd

    plot_aimd(h5file='aimd.h5', show=True)
    '''
    plot_aimd(h5file='aimd.h5', show=True)
