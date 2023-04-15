"""

each dataowners first preprocess its local dataset

"""

import pandas as pd
import numpy as np
import random

# 假设有两个用户DO1, DO2
def get_data():
    data = pd.read_csv('../datasets/winequality-red.csv', sep=';')
    return data

def seperate_data():
    data = get_data()
    # n = random.randint(0, data.shape[0]) #data.shape[0]是data的行数，随机在整体中分隔开
    n = 700
    X = []
    y = []

    # X1 = data.iloc[:n, :-1]
    X1 = data.iloc[:n, :8] # 选取的维度要和FE中的eta一致
    y1 = data.iloc[:n, -1]
    X.append(X1)
    y.append(y1)

    # X2 = data.iloc[n:, :-1]
    X2 = data.iloc[n:, :8] # 选取的维度要和FE中的eta一致
    y2 = data.iloc[n:, -1]
    X.append(X2)
    y.append(y2)
    return X, y

def get_MaxMinN(X = -1):
    """
    :param X: 多个用户数据拼接而成的list，一个三位数组
    :return: 每个用户每一列数据的最大值、最小值、数据个数
    """
    if X == -1: #若未传入数据X，则自己获取
        X, _ = seperate_data()
    X_Max = []
    X_Min = []
    N = []
    for i in range(len(X)): # i是DO的数量
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

