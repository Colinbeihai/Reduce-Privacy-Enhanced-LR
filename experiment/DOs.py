"""

each dataowners first preprocess its local dataset

"""

import pandas as pd
import numpy as np
import random
from TA import TA, public_key
from sklearn.model_selection import KFold

data_path = '../datasets/winequality-red.csv'


# 假设有两个用户DO1, DO2
def get_total_data():
    data = pd.read_csv(data_path, sep=';')
    return data

def simulate_multiusers(data, userNum=2):
    len = data.shape[0]  # data.shape[0]是data的行数
    n = [random.randint(0, len) for _ in range(userNum-1)]
    n.sort()
    n.insert(0, 0)  # 在最前方插入0
    n.append(len)  # 在最后方插入总数
    X, y =[], []
    for i in range(userNum):
        Xi = data.iloc[ n[i]:n[i+1], :-1]
        yi = data.iloc[ n[i]:n[i+1], -1]
        X.append(Xi)
        y.append(yi)
    return X, y


def get_MaxMinN(X=-1):
    """
    :param X: 多个用户数据拼接而成的list，一个三位数组
    :return: 每个用户每一列数据的最大值、最小值、数据个数
    """
    if X == -1:  # 若未传入数据X，则自己获取
        X, _ = simulate_multiusers(get_total_data())
    X_Max = []
    X_Min = []
    N = []
    for i in range(len(X)):  # i是DO的数量
        X_max = []
        X_min = []
        n = len(X[i])
        for column in X[i].columns:
            max = np.max(X[i][column])
            min = np.min(X[i][column])
            X_max.append(max)
            X_min.append(min)
        X_Max.append(X_max)
        X_Min.append(X_min)
        N.append(n)
    return X_Max, X_Min, N

def normalize_global(X, g_max, g_min):
    """
    根据全局最大最小值对每个用户的数据进行归一化
    :return: 全局归一化之后数据
    """
    wide = []
    for i in range(len(g_max)):
        _range = g_max[i] - g_min[i]
        wide.append(_range)
    for num in range(len(X)):
        data = X[num]
        for i in range(len(data.columns)):
            data.iloc[:, i] = (data.iloc[:, i] - g_min[i]) / wide[i]
        X[num] = data
    return X

def extend_sample(sample):
    '''
    DOi extend each sample data into a matrix
    sample data: x1, x2, ..., xd, y
    matrix shape: (d+1)*(d+2)
    :return:matrix
    '''
    d = len(sample) - 1
    x = sample[:d]
    y = sample[-1]
    x.insert(0, 1) # 在列表x中0的位置上插入1
    M = []
    for item in x:
        x_k = np.multiply(item, x)
        M.append(x_k)
    M.append( np.multiply(x, y) )
    M = pd.DataFrame(M)
    M = M.T
    return M

def extend_to_matrix(X):
    """
    获得归一化后的数据，并将其扩展为一个矩阵
    :param X: 全局归一化之后的训练数据
    :return: M
    """
    M = []
    for xi in X:
        Mi = []
        for row in xi.iterrows():
            sample = list(row[1]) # iterrows()的用法，返回元组，row[0]是行号，row[1]是对应数据
            Mik = extend_sample(sample)
            Mi.append(Mik)

        mi = pd.DataFrame(np.zeros(Mi[0].shape),
                          columns=Mi[0].columns, index=Mi[0].index)
        for Mik in Mi:
            mi = mi.add(Mik) # 将三位矩阵中二维矩阵对应元素相加，得到求和后的二维矩阵
        M.append(mi)
    return M

def encrypt_data(M):
    """
    将本地数据加密
    :param M: 逐个，拓展后的数据矩阵
    :return: 密文数据，对应的明文是归一化之后的
    """
    pk = public_key()
    c = 1000 # 常数，将小数转为整数用
    en_M = []
    for mi in M:
        en_Mi = []
        for row in mi.iterrows():
            plain = list(row[1])
            # 将mi由有理数转为整型，通过乘一个大数再取整完成
            plain = np.multiply(plain, c)
            plain = list(map(int, plain))
            # 转换整数之后按行加密
            cipher = TA.encrypt(pk, plain)
            gr = cipher['ct0']
            en = list(cipher['ct_list'])
            en.insert(0, gr)
            en_Mi.append(en)
        en_M.append(en_Mi)
    return en_M