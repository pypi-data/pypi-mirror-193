import pandas as pd
import itertools
import math

import numpy as np
import random
import multiprocessing
import os, sys
import time
import os

import copy
from multiprocessing import Process

def readfile(path):
    dataframe = pd.read_csv(path, header=None, delimiter="/0", engine='python')  # 文件地址
    initial_information = dataframe
    # print (initial_information[5][2])
    return initial_information



def mkdir(path):
    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("\\")
    # path = path.rstrip("//")
    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists = os.path.exists(path)
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path)
        print(path + ' 创建成功')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print(path + ' 目录已存在')
        return False  # 读取文件内容并打印

def save_sample(samp, path):
    print('saving simple')
    filePath = os.getcwd()
    dictionay = filePath + path + "//"
    mkdir(dictionay)
    for i in range(0, len(samp)):
        t = dictionay + "sample" + str(i)
        data_list = samp[i]
        # convert list to array
        # data_array = np.array(data_list)
        # print(type(data_array))
        # saving...
        f = open(t, 'w')
        for k in data_list:
            for j in k:
                f.write(str(j))
                f.write(',')
            f.write('\n')
        f.close()
        # np.savetxt(t, data_array, delimiter=',')
        if i % (len(samp) / 10) == 0:
            print(i / len(samp) * 100, "%", end="")

