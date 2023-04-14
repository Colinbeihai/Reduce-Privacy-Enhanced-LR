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
    Mi = []
    for xi in X:
        for row in xi.iterrows():
            sample = list(row[1]) # iterrows()的用法，row[0]是行号，row[1]是对应数据
            Mik = extend_sample(sample)
            Mi.append(Mik)
    # 当第二个循环后，Mi不断拓展数据，最后变为M
    return Mi

def encrypt_data():
    """
    将本地数据加密
    :return: 密文数据，对应的明文是归一化之后的
    """
    pk = public_key()
    M = extend_sample()
    X_gnorm = 1+1
    for X_i in X_gnorm:
        for i in range(len(X_i)):
            en_X = TA.encrypt(pk, X_i.iloc[i]) # 返回的是字典
            X_i.iloc[i] = en_X['ct_list']
    return X_gnorm

def upload_data():
    """
    将本地数据加密，上传
    :return: 密文数据，对应的明文是归一化之后的
    """
    pk = public_key()
    X_gnorm = normalize_global()
    for X_i in X_gnorm:
        for i in range(len(X_i)):
            en_X = TA.encrypt(pk, X_i.iloc[i]) # 返回的是字典
            X_i.iloc[i] = en_X['ct_list']
    return X_gnorm

def str_to_int(numbers):
    numbers = list(map(int, numbers))  # 把字符串型转为数值型，注意这里转的是整数
    return numbers

X = normalize_global()
print(X)