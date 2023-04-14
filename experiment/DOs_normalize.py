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

def upload_data():
    """
    将本地数据加密，上传
    :return: 密文数据，对应的明文是归一化之后的
    """
    pk = public_key()
    X_gnorm = normalize_global()
    for X_i in X_gnorm:
        for i in range(len(X_i)):
            en_X = TA.encrypt(pk, X_i.iloc[i]) #返回的是字典
            X_i.iloc[i] = en_X['ct_list']
    return X_gnorm

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

# 调试用
# x =  [random.uniform(-0.05, 1.05) for _ in range(9)]
# M = extend_sample(x)

# X = upload_data()

