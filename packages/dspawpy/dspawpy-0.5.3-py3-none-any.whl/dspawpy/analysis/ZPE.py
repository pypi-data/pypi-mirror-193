# 公司: 鸿之微
# 作者: 黄庆亮
# 开发时间: 2022/11/1 17:05
#import math
#x = min(5,10,15)
#y = max(5,10,15)#min()和max()函数可用于查找可迭代的最小值或最大值
#print(x)
#print(y)
#z=abs(-6)#abs()函数返回指定数字的绝对(正)值
#print(z)
#A = pow(4,3) # A等于4的三次方
#print(A)
def thermo_correction(fretxt:str='frequency.txt', T:float=298.15):
    """从fretext中读取数据，计算ZPE和TS

    输入
    ----------
    fretxt : str, 可选
        记录频率信息的文件所在路径, 默认当前路径下的'frequency.txt'
    T : float, 可选
        温度，单位K, 默认298.15

    输出
    ----------
    ZPE: float
        零点能
    TS: float
        熵校正
    """
    import numpy as np
    import os

    # 1. read data
    data_get_ZPE=[]
    data_get_TS = []

    with open(fretxt,'r') as f:
        for line in f.readlines():
            data_line = line.strip().split()
            if len(data_line) != 6:
                continue
            if data_line[1] == "f":
                data_get_ZPE.append(float(data_line[5]))
                data_get_TS.append(float(data_line[2]))

    data_get_ZPE = np.array(data_get_ZPE)
    data_get_TS = np.array(data_get_TS)
    
    # 2. printout to check
    print(f'=== 从{fretxt}中读取到的相关如下 ===')
    print('    ZPE(meV) \t TS(THz)：')
    for i in range(len(data_get_ZPE)):
        print(' ', data_get_ZPE[i],'\t',data_get_TS[i])
    print('-'*40)

    if len(data_get_ZPE) == 0:
        raise ValueError('全是虚频，请考虑重新优化结构...')
    else:
        print('正在写入ZPE_TS.dat文件...')
        np.savetxt('ZPE_TS.dat', np.array([data_get_ZPE, data_get_TS]).T, fmt='%.6f', header='ZPE(meV) \t TS(THz)', comments=f'Data read from {os.path.abspath(fretxt)}\n')

    # 3. calculate
    ZPE = 0
    for data in data_get_ZPE:
        ZPE += data / 2000.0
    print('\n--> 零点振动能为：',ZPE)

    # T = 298.15 #温度 单位：K
    # S = 0
    Na = 6.02214179E+23 #阿伏伽德罗常数 单位 /mol
    h = 6.6260696E-34 #普朗克常数 单位J*s
    kB = 1.3806503E-23#玻尔兹曼常数 J/K
    R = Na*kB # 理想气体常数 J/(K*mol)
    # THz = 1e+12 # 1 Hz = 1e+12 THz
    # e = 1.60217653E-19 #单位 C

    sum_S = 0
    import math #因为要使用 e的多少次方，ln（）对数
    for vi_THz in data_get_TS:
        vi_Hz = vi_THz * 1e+12
        m1 = h*Na*vi_Hz
        m2 = h*vi_Hz/(kB*T)
        m3 = math.exp(m2)-1
        m4 = T* m3
        m5 = 1-math.exp(-m2)    #math.exp(3) 就是e的3次方
        m6 = math.log(m5,math.e)  # m6= ln(m5)   math.e在python中=e ，以右边为底的对数
        m7 = R * m6
        m8 = m1/m4-m7    #S 单位J/(mol*K)
        m9 = (T*m8/1000)/96.49     #T*S,将单位化为KJ/mol, 96.49 kJ/mol = 1 eV 单位eV
        sum_S += m9

    print('--> TS为：',sum_S)

    with open('ZPE_TS.dat', 'a') as f:
        f.write(f'\n--> ZPE: {ZPE}')
        f.write(f'\n--> TS: {sum_S}\n')

    return ZPE, sum_S 

if __name__ == '__main__':
    import sys
    if len(sys.argv) == 1:
        thermo_correction()
    elif len(sys.argv) == 2:
        thermo_correction(sys.argv[1])
    elif len(sys.argv) == 3:
        thermo_correction(sys.argv[1], float(sys.argv[2]))
    else:
        print('命令行使用方法：\n $ python ZPE.py [fretxt] [T] \n')
        raise ValueError('参数输入错误')

    '''
    from dspawpy.analysis.ZPE import thermo_correction

    fretxt = 'frequency.txt' # 指定频率信息文本文件所在路径
    T = 298.15 # 指定温度，单位K
    ZPE, sum_S = thermo_correction(fretxt, T) # 获取ZPE和TS
    '''