import numpy as np
import pandas as pd

from DOs import *
from TA import *

def normalize_global():
    """
    根据全局最大最小值对每个用户的数据进行归一化
    :return: 全局归一化之后数据
    """
    X, _ = seperate_data()
    # print(f'before glo_norm{X}')
    g_max, g_min = XMax_Xmin()  #得到的最大最小值包含小噪声
    wide = []
    for i in range(len(g_max)):
        _range = g_max[i] - g_min[i]
        wide.append(_range)
    for num in range(len(X)):
        data = X[num]
        for i in range(len(data.columns)):
            data.iloc[:, i] = (data.iloc[:, i] - g_min[i]) / wide[i]
        X[num] = data
    # print(f'before glo_norm{X}')
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

def extend_to_matrix():
    """
    获得归一化后的数据，并将其扩展为一个矩阵
    :return: M
    """
    X = normalize_global()
    M = []
    for xi in X:
        Mi = []
        for row in xi.iterrows():
            sample = list(row[1]) # iterrows()的用法，返回元组，row[0]是行号，row[1]是对应数据
            Mik = extend_sample(sample)
            Mi.append(Mik)
         # 当第二个循环后，Mi不断拓展数据，最后变为M
        M.append(Mi)
    return M

def encrypt_data():
    """
    将本地数据加密
    :return: 密文数据，对应的明文是归一化之后的
    """
    pk = public_key()
    M = extend_to_matrix()
    c = 1000 # 常数，将小数转为整数用
    en_M = []
    for Mi in M:
        mi = pd.DataFrame(np.zeros(Mi[0].shape),
                          columns=Mi[0].columns, index=Mi[0].index)
        for Mik in Mi:
            mi = mi.add(Mik) # 将三位矩阵中二维矩阵对应元素相加，得到求和后的二维矩阵
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

def upload_data():
    """
    上传密文数据
    :return: 要训练的密文
    """
    cipher_data = encrypt_data()
    return cipher_data
