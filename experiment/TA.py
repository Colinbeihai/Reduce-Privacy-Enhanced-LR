from crypto.paillier_FE import FE
from DOs import *
import random
import numpy as np

d = 7
eta = d+2
sec_param = 1024

TA = FE(eta, sec_param)

def public_key():
    '''
    分发公钥给DOs
    :return: public key
    '''
    return TA.generate_public_key()

def master_key(y):
    '''
    分发主私钥给CSs,需要CS提供y
    :return: master key
    '''
    return TA.generate_private_key(y)

def get_GlobalMaxMin():
    """
    进行全局的最大、最小值计算，并对所有样本数求和
    :return: Global X_max, Global X_min, total number of samples
    """
    Max, Min, N = get_MaxMinN()
    g_max = []
    g_min = []
    T_Max = list(zip(*Max)) #转置同时转换为列表，zip函数是两个序列组合，返回一个元组列表
    for tuple in T_Max:
        _Max = max(tuple)
        g_max.append(_Max)
    T_Min = list(zip(*Min)) #转置同时转换为列表，zip函数是两个序列组合，返回一个元组列表
    for tuple in T_Min:
        _Min = min(tuple)
        g_min.append(_Min)
    g_max, g_min = add_noise(g_max, g_min) #加噪声
    g_n = sum(N)
    return g_max, g_min, g_n

def add_noise(max, min):
    n = len(min)
    noise = [random.uniform(-0.05, 0.05) for _ in range(n)]
    max = np.add(max, noise)
    min = np.add(min, noise)
    return max, min

def XMax_Xmin():
    """
    发给用户，让其进行全局的归一化
    :return: Global X_max, Global X_min
    """
    g_max, g_min, _ = get_GlobalMaxMin()
    return g_max, g_min

def total_samples():
    """
    发给服务器，告知其所有用户的样本数量和
    :return: total number of samples
    """
    _, _, g_n = get_GlobalMaxMin()
    return g_n
