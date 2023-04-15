'''

aggregate the ciphertext from DOs and decrypting

'''
import pandas as pd
import numpy as np
from TA import total_samples, public_key, Decrypt
from DOs_normalize import upload_data
from CS1 import deliever_cita, get_skf

alpha = 0.01
# n = total_samples()

def re_aggregation():
    M = upload_data()
    M0 = pd.DataFrame(M[0]) # 取一个元素出来，按照同样形式创建DataFrame
    aggM = pd.DataFrame(np.ones(M0.shape, dtype=int),
                    columns=M0.columns, index=M0.index) # 同型全1矩阵，方便做乘法
    for Mi in M:
        # 由于加密算法的加法同态，密文相乘等于明文相加
        # 但因为此时密文数值都是以字符串形式存放，这里逐个转为整型运算
        for i in range(aggM.shape[0]):
            for j in range(aggM.shape[1]):
                aggM.iloc[i, j] = int(aggM.iloc[i, j]) * int(Mi[i][j])

    return aggM

def iter_train():
    M = re_aggregation()
    mpk = public_key()
    skf = get_skf() # 从CS1处获取由权重向量生成的功能密钥
    de_M = []
    for i in range(M.shape[0]): # 按照DF的行遍历
        ct = {'ct0':M.iloc[i, 0], 'ct_list':M.iloc[i, 1:]}
        # y = cita # 这里的y是cita（权重向量）
        # de_m = Decrypt(skf, y, ct) # 疑惑 skf根据cita生成的，并且CS1也有msk，cita也传过去，那就无需生成skf了
        # de_M.append(de_m)


aggM = re_aggregation()

