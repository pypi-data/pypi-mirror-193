import numpy as np
import datetime
import random


def initial_stru(P, NX, NY, NZ, ion_num):  ### ion_num存放的是迁移离子的个数
    ### 函数功能： 随机掺杂无机物

    x, y, z = np.mgrid[0:NX, 0:NY, 0:NZ]
    x1, y1, z1 = np.mgrid[0:NX - 1, 0:NY - 1, 0:NZ - 1]

    # framework_coords存放体系所有骨架离子的逻辑坐标
    framework_coords = np.zeros((NX, NY, NZ, 3), dtype=int)
    framework_coords[:, :, :, 0] = x
    framework_coords[:, :, :, 1] = y
    framework_coords[:, :, :, 2] = z
    print('体系所有骨架离子的逻辑坐标:',framework_coords)

    ### site_logic_coord存放的是空位的逻辑坐标
    site_logic_coord = np.zeros((NX - 1, NY - 1, NZ - 1, 3),dtype=int)
    site_logic_coord[:, :, :, 0] = x1
    site_logic_coord[:, :, :, 1] = y1
    site_logic_coord[:, :, :, 2] = z1
    print('体系中所有空位对应的逻辑坐标：', site_logic_coord)

    #vacancysite_logic_coor1是将site_logic_coord重新塑形为一维数组
    vacancysite_logic_coor1 = site_logic_coord.reshape((NX - 1) * (NY - 1) * (NZ - 1), 3)

    # occupy_site_coord离子占据的空位编号
    occupy_site_coord = np.random.choice((NX - 1) * (NY - 1) * (NZ - 1), ion_num, replace=False)
    print('walkers所在的空位编号:',occupy_site_coord)
    ion_logic_coor = vacancysite_logic_coor1[occupy_site_coord]
    print('walkers所在的空位坐标:',ion_logic_coor)

    # occupy_number表示被无机物掺杂的骨架离子编号
    occupy_number = np.random.choice(NX * NY * NZ, int(P * NX * NY * NZ), replace=False)
    print('无机物掺杂的骨架离子编号:',occupy_number)

    # coord_doped_label框架离子的位点掺杂标记,以NX*NY*NZ的形式存放
    coord_doped_label = np.zeros((NX, NY, NZ, 1), dtype=int)

    # cllist将掺杂标记重新塑形为一维数组形式
    cllist = coord_doped_label.reshape((NX * NY * NZ))
    # 根据被掺杂的骨架编号 将cllist对应标号的标记为1或0
    cllist[occupy_number] = 1

    # print('骨架离子被无机物掺杂的标记：',coord_doped_label)
    # print('离子初始逻辑坐标：',ion_logic_coor)
    # print('体系所有占点的物理坐标：',site_logtophy_coord)

    initial_cell_coor = np.zeros(ion_num * 3, dtype=int).reshape(ion_num, 3)
    # print(initial_cell_coor)

    return coord_doped_label, ion_logic_coor,initial_cell_coor   ### 同时返回骨架逻辑坐标对应的标记，初始化的离子逻辑坐标,体系所有占点的物理坐标


if __name__ == '__main__':
    time1 = datetime.datetime.now()
    N = 5
    NX = NY = NZ = N
    P = 0.3

    ion_num = 5
    tao_a = 2
    tao_b = 20000
    tao_c = 5000
    rate_hopping_a = float(1 / tao_a)
    rate_hopping_b = float(1 / tao_b)
    rate_hopping_c = float(1 / tao_c)

    aa = initial_stru(P, NX, NY, NZ, ion_num)

    print('第一个函数没问题')

    time2 = datetime.datetime.now()
    print('所花时间：', time2 - time1)
    # time2 = datetime.datetime.now()
    # print('所花时间：', time2 - time1)
    # # print(bb[0][0][0]) ## [1 1 1]
    # # print(bb[1][0][0]) ## [3 1 1]
    # # print(bb[0][1][0]) ## [1 3 1]
    # # print(bb[1][1][0]) ## [3 3 1]
    # # print(bb[1][1][1]) ## [3 3 3]
