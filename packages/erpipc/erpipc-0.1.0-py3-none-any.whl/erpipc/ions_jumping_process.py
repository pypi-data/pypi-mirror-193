import numpy as np
import datetime
import random
from .initial_structure import initial_stru


def ions_jump(rate_hopping_a, rate_hopping_b, rate_hopping_c, coor_doped_label,ions_logic_coor,initial_cell_coor1,NX,NY,NZ):
    ### ions_logic_coor指离子所在的逻辑坐标  coor_doped_label表示所有占点逻辑坐标对应的标记
    ### 函数功能：返回每个空位的实际坐标，每个空位周围各个方向的跳跃概率
    all_cell_logic_coor = []
    all_ion_tao = []
    dxyz = np.array([[0, 0, 0],[0, 0, 1],[0, 1, 0],[0, 1, 1],[1, 0, 0],[1, 0, 1],[1, 1, 0],[1, 1, 1]])
    # print('离子初始逻辑坐标：', ions_logic_coor)
    # print('离子初始胞坐标：',initial_cell_coor1)
    all_turn = []
    for i in np.arange(len(ions_logic_coor)):  ### 遍历体系中的离子逻辑坐标
        i_cor_all = ions_logic_coor[i]+dxyz
        # print('该离子周围的邻居位点逻辑坐标:',i_cor_all)
        i_doped = np.zeros((8, ), dtype=int)
        for j in range(8):
            if coor_doped_label[i_cor_all[j][0], i_cor_all[j][1],i_cor_all[j][2]] == 1:
                i_doped[j] = 1

        i_doped_num = np.zeros((6, ), dtype=int)
        i_doped_num[0] = i_doped[4:8].sum()  ## 空位前方被离子占据的位点个数
        i_doped_num[1] = i_doped[0:4].sum()  ## 空位后方被离子占据的位点个数
        i_doped_num[2] = i_doped[1:8:2].sum()  ## 空位上方被离子占据的位点个数
        i_doped_num[3] = i_doped[0:8:2].sum()  ## 空位下方被离子占据的位点个数
        i_doped_num[4] = i_doped[0:2].sum() + i_doped[4:6].sum()  ## 空位上方被离子占据的位点个数
        i_doped_num[5] = i_doped[2:4].sum() + i_doped[6:8].sum()  ## 空位上方被离子占据的位点个数

        # print('离子周围6个方向的掺杂情况：',time_2 - time_1)
        i_tao = []
        for j in np.arange(len(i_doped_num)):
            if i_doped_num[j] == 0:
                i_tao = np.append(i_tao, rate_hopping_c)  ###0.0002   5000
                # print('该方向跳跃概率：',i_tao[j])
            elif i_doped_num[j] == 4:
                i_tao = np.append(i_tao, rate_hopping_b)  ### 0.00005   20000
                # print('该方向跳跃概率：',i_tao[j])
            else:
                i_tao = np.append(i_tao, rate_hopping_a)  ### 0.5  2
                # print('该方向跳跃概率：',i_tao[j])

        tao_i_sum = i_tao.sum()
        random_decimals = random.uniform(0, 1)
        W_R = tao_i_sum * random_decimals
        # print('随机数',random_decimals,'\n','乘积',W_R)

        if 0 <= W_R and W_R < i_tao[0]:
            turn_n = 'front'
            choose_n = i_tao[0]
            cell_logic_coor = np.array(
                [np.divmod(ions_logic_coor[i][0] + 1, NX - 1), np.divmod(ions_logic_coor[i][1], NY - 1),
                 np.divmod(ions_logic_coor[i][2], NZ - 1)]).T

        elif i_tao[0] <= W_R and W_R < i_tao[0:2].sum():
            turn_n = 'behind'
            choose_n = i_tao[1]
            cell_logic_coor = np.array(
                [np.divmod(ions_logic_coor[i][0] - 1, NX - 1), np.divmod(ions_logic_coor[i][1], NY - 1),
                 np.divmod(ions_logic_coor[i][2], NZ - 1)]).T

        elif i_tao[0:2].sum() <= W_R and W_R < i_tao[0:3].sum():
            turn_n = 'up'
            choose_n = i_tao[2]
            cell_logic_coor = np.array(
                [np.divmod(ions_logic_coor[i][0], NX - 1), np.divmod(ions_logic_coor[i][1], NY - 1),
                 np.divmod(ions_logic_coor[i][2] + 1, NZ - 1)]).T

        elif i_tao[0:3].sum() <= W_R and W_R < i_tao[0:4].sum():
            turn_n = 'down'
            choose_n = i_tao[3]
            cell_logic_coor = np.array(
                [np.divmod(ions_logic_coor[i][0], NX - 1), np.divmod(ions_logic_coor[i][1], NY - 1),
                 np.divmod(ions_logic_coor[i][2] - 1, NZ - 1)]).T

        elif i_tao[0:4].sum() <= W_R and W_R < i_tao[0:5].sum():
            turn_n = 'left'
            choose_n = i_tao[4]
            cell_logic_coor = np.array(
                [np.divmod(ions_logic_coor[i][0], NX - 1), np.divmod(ions_logic_coor[i][1] - 1, NY - 1),
                 np.divmod(ions_logic_coor[i][2] + 1, NZ - 1)]).T

        elif i_tao[0:5].sum() <= W_R and W_R < i_tao[:].sum():
            turn_n = 'right'
            choose_n = i_tao[5]
            cell_logic_coor = np.array(
                [np.divmod(ions_logic_coor[i][0], NX - 1), np.divmod(ions_logic_coor[i][1] + 1, NY - 1),
                 np.divmod(ions_logic_coor[i][2], NZ - 1)]).T

        all_turn.append(turn_n)  ## 离子跳跃方向的跳跃概率
        all_cell_logic_coor.append(cell_logic_coor)  ### 离子新的胞坐标和逻辑坐标
        all_ion_tao = np.append(all_ion_tao, 1 / choose_n)  ### 所有离子跳跃一次花的时间步长

    all_cell_logic_coor1 = np.array(all_cell_logic_coor)
    all_cell_coor = all_cell_logic_coor1[:,0]
    all_logic_coor = all_cell_logic_coor1[:,1]
    all_next_ion_phycoor1 = all_logic_coor + (NZ-1)*(all_cell_coor+initial_cell_coor1)


    # print('离子胞坐标的变化', all_cell_logic_coor1[:,0])
    # print('新的离子逻辑坐标：', all_logic_coor)
    # print('离子得到的新的胞坐标：',all_cell_coor + initial_cell_coor1)
    # print('新的离子物理坐标：', all_next_ion_phycoor1)

    # print('离子跳跃方向：', all_turn)
    # print('离子的跳跃时长：', all_ion_tao)
    return all_logic_coor, all_cell_coor,all_ion_tao, all_next_ion_phycoor1


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
    # print('aa[0]',aa[0])
    # print('aa[1]',aa[1])
    # print('aa[2]',aa[2])
    print('第一个函数没问题')

    bb = ions_jump(rate_hopping_a, rate_hopping_b, rate_hopping_c, aa[0],aa[1], aa[2],NX,NY,NZ)
    print('第二个函数没问题')
    time2 = datetime.datetime.now()
    print('所花时间：', time2 - time1)
    # time2 = datetime.datetime.now()
    # print('所花时间：', time2 - time1)
    # # print(bb[0][0][0]) ## [1 1 1]
    # # print(bb[1][0][0]) ## [3 1 1]
    # # print(bb[0][1][0]) ## [1 3 1]
    # # print(bb[1][1][0]) ## [3 3 1]
    # # print(bb[1][1][1]) ## [3 3 3]
