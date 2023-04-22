from crypto.paillier_FE import FE
import random
import numpy as np

d = 10
eta = d + 2
sec_param = 1024

TA = FE(eta, sec_param)


class TrustedAuthority(FE):
    def __init__(self, eta, sec_param):
        super(TrustedAuthority, self).__init__(eta, sec_param)

    def public_key(self):
        '''
        分发公钥给DOs
        :return: public key
        '''
        return self.generate_public_key()

    def get_msk(self):
        """
        获得master secret key
        :return: msk
        """
        return self.msk

    def SKGenerate(self, y):
        '''
        分发主私钥给CSs,需要CS提供y
        :return: master key
        '''
        return self.generate_private_key(y)

    def Decrypt(self, sk, y, ct):
        """
        CS2用来对聚合后的M逐行解密
        :param sk: 功能私钥
        :param y: 权重向量
        :param ct: 加密后的值，字典类型，包含'ct0'和'ct_list'
        :return:
        """
        return self.decrypt(sk, y, ct)

    def get_GlobalMaxMin(self, Max, Min, N):
        """
        进行全局的最大、最小值计算，并对所有样本数求和
        :return: Global X_max, Global X_min, total number of samples
        """
        g_max = []
        g_min = []
        T_Max = list(zip(*Max))  # 转置同时转换为列表，zip函数是两个序列组合，返回一个元组列表
        for tuple in T_Max:
            _Max = max(tuple)
            g_max.append(_Max)
        T_Min = list(zip(*Min))  # 转置同时转换为列表，zip函数是两个序列组合，返回一个元组列表
        for tuple in T_Min:
            _Min = min(tuple)
            g_min.append(_Min)
        g_max, g_min = add_noise(g_max, g_min)  # 加噪声
        g_n = sum(N)
        return g_max, g_min, g_n


    def XMax_Xmin(self, Max, Min, N):
        """
        发给用户，让其进行全局的归一化
        :return: Global X_max, Global X_min
        """
        g_max, g_min, _ = self.get_GlobalMaxMin(Max, Min, N)
        return g_max, g_min


    def total_samples(self, N):
        """
        发给服务器，告知其所有用户的样本数量和
        :return: total number of samples
        """
        g_n = sum(N)
        return g_n

    def get_skf(self, cita):
        '''
        由cita向量生成功能密钥，随后给CS2
        :return: 功能密钥skf
        '''
        return self.SKGenerate(cita)


def add_noise(max, min):  # 添加噪声
    n = len(min)
    noise = [random.uniform(-0.05, 0.05) for _ in range(n)]
    max = np.add(max, noise)
    min = np.add(min, noise)
    return max, min
