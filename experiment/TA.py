from crypto.paillier_FE import FE
from DOs import *
import random

d = 7
eta = d+2
sec_param = 1024

TA = FE(eta, sec_param)

def public_key():
    '''
    分发公钥给DOs
    :return: public key
    '''
    return TA.generate_public_key()

def master_key(y):
    '''
    分发主私钥给CSs
    需要CS提供y
    :return: master key
    '''
    return TA.generate_private_key(y)

def get_GlobalMaxMin():
    max, min, n = get_MaxMinN()
    return max, min, n

def add_noise():
    max, min, n = get_GlobalMaxMin()
    noise = [random.uniform(-0.05, 0.05) for _ in range(n)]
    max = max+noise
    min = min+noise
    return max, min

