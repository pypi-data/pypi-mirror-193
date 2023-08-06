import numpy as np
import datetime
from .initial_structure import initial_stru
from .ions_jumping_process import ions_jump
from .samples_to_generate import sample_generation
from .file_hand import mkdir

def calculate_parameter(ion_all_cor,all_ion_time,ion_num,jump_num):## walkers迁移步数用参数设置
    # ion_all_cor是离子跳跃过程所有物理坐标

    delta_r_2 = []
    delta_t_2 = []
    # for i in np.arange(len(ion_all_cor)-20000):
    for i in np.arange(len(ion_all_cor) - int(jump_num/5)*1):
        delta_r_i = ((ion_all_cor[i] - ion_all_cor[i+int(jump_num/5)*1]) ** 2).sum(axis=1)
        delta_t_i = all_ion_time[i:i+int(jump_num/5)*1].sum(axis=0)
        delta_r_2 = np.append(delta_r_2,delta_r_i)
        delta_t_2 = np.append(delta_t_2,delta_t_i)
    # print('delta_r_2:',delta_r_2)
    # print('delta_t_2:',delta_t_2)
    msd_t_2 = (delta_r_2/delta_t_2).reshape(len(ion_all_cor)-int(jump_num/5)*1,ion_num)
    msd_t_2_ave = msd_t_2.mean(0)
    # print('delta_r_2',msd_t_2)
    # print('平均：', msd_t_2_ave)
    delta_r_4 = []
    delta_t_4 = []
    for i in np.arange(len(ion_all_cor)-int(jump_num/5)*2):
        delta_r_i = ((ion_all_cor[i] - ion_all_cor[i+int(jump_num/5)*2]) ** 2).sum(axis=1)
        delta_t_i = all_ion_time[i:i+int(jump_num/5)*2].sum(axis=0)
        delta_r_4 = np.append(delta_r_4,delta_r_i)
        delta_t_4 = np.append(delta_t_4,delta_t_i)
    # print('delta_r_4:',delta_r_4)
    # print('delta_t_4:',delta_t_4)
    msd_t_4 = (delta_r_4/delta_t_4).reshape(len(ion_all_cor)-int(jump_num/5)*2,ion_num)
    msd_t_4_ave = msd_t_4.mean(0)
    # print('delta_r_4',msd_t_4)
    # print('平均：', msd_t_4_ave)
    delta_r_6 = []
    delta_t_6 = []
    for i in np.arange(len(ion_all_cor)-int(jump_num/5)*3):
        delta_r_i = ((ion_all_cor[i] - ion_all_cor[i+int(jump_num/5)*3]) ** 2).sum(axis=1)
        delta_t_i = all_ion_time[i:i+int(jump_num/5)*3].sum(axis=0)
        delta_r_6 = np.append(delta_r_6,delta_r_i)
        delta_t_6 = np.append(delta_t_6,delta_t_i)
    # print('delta_r_6:',delta_r_6)
    # print('delta_t_6:',delta_t_6)
    msd_t_6 = (delta_r_6/delta_t_6).reshape(len(ion_all_cor)-int(jump_num/5)*3,ion_num)
    msd_t_6_ave = msd_t_6.mean(0)
    # print('delta_r_6',msd_t_6)
    # print('平均：', msd_t_6_ave)
    delta_r_8 = []
    delta_t_8 = []
    for i in np.arange(len(ion_all_cor)-int(jump_num/5)*4):
        delta_r_i = ((ion_all_cor[i] - ion_all_cor[i+int(jump_num/5)*4]) ** 2).sum(axis=1)
        delta_t_i = all_ion_time[i:i+int(jump_num/5)*4].sum(axis=0)
        delta_r_8 = np.append(delta_r_8,delta_r_i)
        delta_t_8 = np.append(delta_t_8,delta_t_i)
    # print('delta_r_8:',delta_r_8)
    # print('delta_t_8:',delta_t_8)
    msd_t_8 = (delta_r_8/delta_t_8).reshape(len(ion_all_cor)-int(jump_num/5)*4,ion_num)
    msd_t_8_ave = msd_t_8.mean(0)
    # print('delta_r_8',msd_t_8)
    # print('平均：', msd_t_8_ave)
    delta_r_10 = ((ion_all_cor[0] - ion_all_cor[jump_num]) ** 2).sum(axis=1)
    delta_t_10 = all_ion_time.sum(axis=0)
    msd_t_10_ave = delta_r_10/delta_t_10
    # print('delta_r_10:', delta_r_10)
    # print('delta_t_10:', delta_t_10)
    # print('平均：', msd_t_10_ave)
    MSD_T_all = np.array([msd_t_2_ave, msd_t_4_ave, msd_t_6_ave, msd_t_8_ave, msd_t_10_ave])/6
    # print('MSD_T_all',MSD_T_all)
    MSD_T_10_ion = MSD_T_all.mean(axis=0)
    # print('MSD_T_10_ion',MSD_T_10_ion,)
    MSD_6T = MSD_T_10_ion.mean()
    print('体系msd/6t：',MSD_6T)
    return MSD_6T


if __name__ == '__main__':
    time1 = datetime.datetime.now()
    print('time1',time1)

    effect_path = 'sample0'
    mkdir(effect_path)
    N = 50
    NX = NY = NZ = N
    jump_num = 100
    ion_num = 10
    P = 0
    tao_a = 20
    tao_b = 20000
    tao_c = 50000
    rate_hopping_a = float(1 / tao_a)
    rate_hopping_b = float(1 / tao_b)
    rate_hopping_c = float(1 / tao_c)

    msd_6t_n = []
    for i in range(0,10):
        aa = initial_stru(P, NX, NY, NZ,ion_num)
        time2 = datetime.datetime.now()
        print('time2', time2)
        print('结构初始化时间间隔：', time2 - time1)

        cc = sample_generation(jump_num,rate_hopping_a, rate_hopping_b,rate_hopping_c,aa[0],aa[1],aa[2],NX,NY,NZ)
        time3 = datetime.datetime.now()
        print('time3', time3)
        print('样本已生成时间间隔：',time3 - time2)

        dd = calculate_parameter(cc[0],cc[1],ion_num,jump_num)
        msd_6t_n.append(dd)
        # dd.to_csv('sample8.csv', index=False)
        time4 = datetime.datetime.now()
        print('time4', time4)
        print('计算参数时间间隔：', time4 - time3)

        print('总时间：', time4 - time1)
    mean_msd_6t = sum(msd_6t_n)/len(msd_6t_n)
    filename = effect_path + "\\" + 'consequence'
    with open(filename,'w') as file_object:
        # 记录表格第0行的标头的信息
        file_object.write(str(msd_6t_n))
        file_object.write('\n')
        file_object.write(str(mean_msd_6t))






