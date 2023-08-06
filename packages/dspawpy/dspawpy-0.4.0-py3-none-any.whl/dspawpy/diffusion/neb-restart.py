import os
intro = """脚本功能
- 旧00子文件夹 --> 备份文件夹/00/00.tar.xz ...
- 旧01子文件夹 --> 备份文件夹/01/01.tar.xz ...
- ...
- neb.h5 + neb.json --> 备份文件夹/neb.tar.xz
- DS-PAW.log --> 备份文件夹/DS-PAW.log
- 其他的不动
- 旧00 01 ...子文件夹只保留结构 structure00.as structure01.as ...

使用方法：
1. 命令行
    $ python neb-restart.py <output>
2. 脚本中调用
    from neb-restart import restart
    restart(irerctory: str, inputin: str, output: str)
"""


def restart(direrctory: str, inputin: str, output: str):
    """将旧NEB任务归档压缩，并在原路径下准备续算

    Parameters
    ----------
    direrctory : str
        旧NEB任务所在路径，默认当前路径
    inputin : str
        输入参数文件名，默认input.in
    output : str
        备份文件夹路径

    Raises
    ------
    FileNotFoundError
        如果原NEB路径下没有结构文件，抛出异常
    """
    # initialize para
    from neb_utils import get_neb_subfolders

    if output == '':
        raise ValueError('备份文件夹路径不能为空！')
    elif os.path.isdir(output):
        raise ValueError('备份文件夹已存在！')

    if direrctory == '':
        directory = os.getcwd()
    if inputin == '':
        inputin = 'input.in'

    # 读取子文件夹名称列表，仅保留形如00，01数字文件夹路径
    subfolders = get_neb_subfolders(directory)
    # 创建备份文件夹并进入
    os.makedirs(f'{directory}/{output}')
    os.chdir(f'{directory}/{output}')
    # 将-0改成-9可提供极限压缩比
    os.environ["XZ_OPT"] = '-T0 -0'
    for subfolder in subfolders:
        # 备份
        os.system(f'mv {directory}/{subfolder} ./')
        # 准备续算用的结构文件
        os.mkdir(f'{directory}/{subfolder}')
        latestStructureFile = os.path.join(
            directory, output, subfolder, 'latestStructure%s.as' % subfolder)
        structureFile = os.path.join(
            directory, output, subfolder, 'structure%s.as' % subfolder)
        bk_latestStructure = f'{directory}/latestStructure{subfolder}.as'
        bk_structure = f'{directory}/structure{subfolder}.as'

        if os.path.exists(latestStructureFile):
            os.system(  # 复制到子文件夹
                f'cp {latestStructureFile} {directory}/{subfolder}/structure{subfolder}.as')
            # 备份latestStructureFile到主目录
            os.system(f'cp {latestStructureFile} {bk_latestStructure}')
        elif os.path.exists(structureFile):
            print(f'未找到{latestStructureFile}，复用{structureFile}续算')
            os.system(  # 复制到子文件夹
                f'cp {structureFile} {directory}/{subfolder}/structure{subfolder}.as')
        else:
            raise FileNotFoundError(
                f'{latestStructureFile}和{structureFile}都不存在！')
        # 备份structureFile到主目录
        if os.path.exists(structureFile):
            os.system(f'cp {structureFile} {bk_structure}')

        # 压缩和移动文件
        # 若存在latestStructure00.as和structure00.as，则压缩00文件夹并把主结构移入00文件夹
        if os.path.exists(bk_latestStructure) and os.path.exists(bk_structure):
            os.system(
                f"tar -Jcf {subfolder}.tar.xz -C {subfolder} . --remove-files && mkdir {subfolder} && mv {subfolder}.tar.xz {directory}/latestStructure{subfolder}.as {directory}/structure{subfolder}.as {subfolder}/ &")
        # 若仅存在latestStructure00.as，则压缩00文件夹并把主结构移入00文件夹
        elif os.path.exists(bk_latestStructure):
            os.system(
                f"tar -Jcf {subfolder}.tar.xz {subfolder} . --remove-files && mkdir {subfolder} && mv {subfolder}.tar.xz {directory}/latestStructure{subfolder}.as {subfolder}/ &")
        # 若仅存在structure00.as，则压缩00文件夹并把主结构移入00文件夹
        elif os.path.exists(bk_structure):
            os.system(
                f"tar -Jcf {subfolder}.tar.xz -C {subfolder} . --remove-files && mkdir {subfolder} && mv {subfolder}.tar.xz {directory}/structure{subfolder}.as {subfolder}/ &")
        else:  # 如果都不存在，说明备份失败
            raise FileNotFoundError(
                f'{bk_latestStructure}和{bk_structure}都不存在！')

    # 备份neb.h5,neb.json和DS-PAW.log
    if os.path.exists(f'{directory}/neb.json'):
        os.system(
            f'mv {directory}/neb.h5 {directory}/neb.json {directory}/DS-PAW.log ./')
        os.system(f'tar -Jcf neb.tar.xz neb.h5 neb.json --remove-files &')
    else:
        os.system(
            f'mv {directory}/neb.h5 {directory}/DS-PAW.log ./')
        os.system(f'tar -Jcf neb.tar.xz neb.h5 --remove-files &')


if __name__ == '__main__':
    # 在命令行直接运行此脚本时输出下列帮助信息
    print('=========================== DSPAWNEB 续算准备 ===========================')
    print(intro)
    print('========================================================================')
    directory = input('--> 请指定原路径（直接回车默认为当前路径）：')
    inputin = input('--> 请指定参数文件名（直接回车默认为input.in）：')
    bd = input('--> 请指定备份文件夹名字（将在原路径下新建）：')
    print('  正在处理...')
    restart(directory, inputin, bd)
