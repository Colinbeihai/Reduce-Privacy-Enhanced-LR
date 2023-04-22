"""

aggregate the ciphertext from DOs and decrypting

"""
import pandas as pd
import numpy as np
import gmpy2 as gp
import random


class CloudSever:
    def __init__(self, n, d):
        self.alpha = 0.0015
        self.n = n  # 总的数据数
        self.l = 20  # 迭代训练次数
        self.d = d  # 数据维度
        self.cita = np.zeros(d + 1, dtype=int)
        self.cita = np.append(self.cita, -1)

    def re_aggregation(self, M):
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

    def decrypt_inner_product(self, M, skf, TA):
        """
        解密数据，得到结果
        :param M: 要解密的数据
        :return: 逐行解密的结果
        """
        # r = self.r if isinstance(self.r, list) else np.zeros(len(msk), dtype=int) # 若r为初始化的数值0，则将其扩展为矩阵
        # skf = skf + np.dot(r, msk)
        de_M = []
        for i in range(M.shape[0]):  # 按照DF的行遍历
            ct = {'ct0': M.iloc[i, 0], 'ct_list': list(M.iloc[i, 1:])}
            y = self.cita  # 这里的y是cita（权重向量）
            de_m = TA.Decrypt(skf, y, ct)  # 疑惑 skf根据cita生成的，并且CS1也有msk，cita也传过去，那就无需生成skf了
            de_M.append(de_m)
        return de_M

    def iterration_updata(self, M, TA):
        """
        迭代训练权重向量
        :param m_cita: 解密结果，数据m与权重cita的积
        :param d: 数据的维度
        :return:
        """
        for i in range(self.l):
            skf = TA.get_skf(self.cita)
            m_cita = self.decrypt_inner_product(M, skf, TA)
            delta = [x * (self.alpha / self.n) for x in m_cita]
            print(list(delta)[:3])
            self.cita[:-1] = np.subtract(self.cita[:-1], delta)
            print(self.cita)

