'''

CS1 generate the function key for CS2

'''
from TA import total_samples, public_key, SKGenerate
from CS2 import get_delta
import numpy as np
import pandas as pd

num = total_samples()
d = 7
l = 20 # 迭代训练次数

cita = np.zeros(d + 1, dtype=int)
cita = np.append(cita, -1)

def deliver_cita():
    '''
    把cita给CS2,我认为这里不对,若给CS2,不需要自己给它生成功能密钥
    :return: 权重向量cita
    '''
    return cita # 注:做了修改,改为形参传递,此处留着仅便于调试

def get_skf():
    '''
    CS1由cita向量生成功能密钥，随后给CS2
    :return: 功能密钥skf
    '''
    return SKGenerate(cita)

def initialize_cita():
    """
    初始化权重向量
    :return: cita初始值
    """
    cita = np.zeros(d + 1, dtype=int)
    cita = np.append(cita, -1)
    return cita

def iterration_updata():
    '''
    迭代训练权重向量
    :return:
    '''
    global cita
    for i in range(l):
        delta = get_delta(cita)
        cita[:d+1] = np.subtract(cita[:d+1], delta)
        print(cita)

    # 将列表转换为DataFrame对象
    df = pd.DataFrame(cita)
    # 将DataFrame对象保存到本地
    df.to_csv("cita.csv", sep=';', index=False)

if __name__ == '__main__':
    iterration_updata()
