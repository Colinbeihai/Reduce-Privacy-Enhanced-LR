"""

aggregate the ciphertext from DOs and decrypting

"""
import pandas as pd
import numpy as np
import random
import copy
from TA import total_samples, public_key, Decrypt, get_msk, get_skf_fromTA
from DOs_normalize import upload_data
# from CS1 import deliver_cita, get_skf
# from QU import query_answer

alpha = 0.001
n = total_samples()
r = 0  # 噪声向量,用来干扰CS1.收到CS1的消息后抵消上一次干扰
weight = 0  # 本地权重
# skf = get_skf()

def gain_data():
    '''
    从dataOwner哪里得到上传的数据
    :return: 数据
    '''
    M = upload_data()
    return M

def re_aggregation(M):
    if type(M) == list:
        M0 = pd.DataFrame(M[0])  # 取一个元素出来，按照同样形式创建DataFrame
        aggM = pd.DataFrame(np.ones(M0.shape, dtype=int),
                        columns=M0.columns, index=M0.index)  # 同型全1值矩阵，方便做乘法
        for Mi in M:
            # 由于加密算法的加法同态，密文相乘等于明文相加
            # 但因为此时密文数值都是以字符串形式存放，这里逐个转为整型运算
            for i in range(aggM.shape[0]):
                for j in range(aggM.shape[1]):
                    aggM.iloc[i, j] = int(aggM.iloc[i, j]) * int(Mi[i][j])
    elif isinstance(M, pd.DataFrame):
        aggM = M
    return aggM

def decrypt_inner_product(cita, M):
    """
    解密数据，得到结果
    :param cita: 权重
    :param M: 要解密的数据
    :return: 逐行解密的结果
    """
    global r, weight
    weight = copy.deepcopy(cita)
    msk = get_msk()
    skf = get_skf_fromTA(weight) # 从CS1处获取由权重向量生成的功能密钥
    r = r if isinstance(r, list) else np.zeros(len(msk), dtype=int) # 若r为初始化的数值0，则将其扩展为矩阵
    skf = skf + np.dot(r, msk)
    de_M = []
    for i in range(M.shape[0]):  # 按照DF的行遍历
        ct = {'ct0': M.iloc[i, 0], 'ct_list': list(M.iloc[i, 1:])}
        y = weight  # 这里的y是cita（权重向量）
        de_m = Decrypt(skf, y, ct)  # 疑惑 skf根据cita生成的，并且CS1也有msk，cita也传过去，那就无需生成skf了
        de_M.append(de_m)
    return de_M


def send_blind_result(cita):
    """
    生成变化量,同时增加噪声来干扰
    :return:噪声干扰后的权重修正值
    """
    M_ = gain_data()
    M = re_aggregation(M_)
    m_cita = decrypt_inner_product(cita, M)
    global r
    r = [random.randint(-2, 2)       for _ in range(len(m_cita))]  # 整数噪声
    # r = [random.uniform(-0.5, 0.5) for _ in range(len(m_cita))] # 浮点数噪声
    delta = [x * (alpha/n) for x in m_cita]
    delta = np.add(delta, r)
    r = np.append(r, -1)  # 对r的维度修正
    # print(list(delta))
    return delta

def get_delta(cita):
    '''
    给CS1发送训练结果
    :return: 权重变化量
    '''
    delta = send_blind_result(cita)
    return delta
    """
    给QU解密的函数
    :param cita: 权重
    :param M: 要解密的数据
    :return: 逐行解密的结果
    """
    weight = copy.deepcopy(cita)
    skf = get_skf_fromTA(weight) # 从CS1处获取由权重向量生成的功能密钥
    de_M = []
    M = pd.DataFrame(M)
    for i in range(M.shape[0]):  # 按照DF的行遍历
        ct = {'ct0': M.iloc[i, 0], 'ct_list': list(M.iloc[i, 1:])}
        y = weight  # 这里的y是cita（权重向量）
        de_m = Decrypt(skf, y, ct)  # 疑惑 skf根据cita生成的，并且CS1也有msk，cita也传过去，那就无需生成skf了
        de_M.append(de_m)
    return de_M