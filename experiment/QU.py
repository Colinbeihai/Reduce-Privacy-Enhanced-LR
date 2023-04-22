"""

send a query request to CSs

"""
import pandas as pd
import numpy as np
from DOs_normalize import encrypt_query
# from CS1 import deliver_cita
from CS import decrypt_query

def prepare_unlabled():
    data = pd.read_csv('../datasets/winequality-red.csv', sep=';')
    unlabled = data.iloc[20:30, :8]
    return unlabled

cita = [ 2, -7,  1, -1,  1, -2,  5, -9, -1]

def query_answer():
    unlabled = prepare_unlabled()
    en_data = encrypt_query(unlabled)

    # cita = pd.read_csv("cita.csv", sep=";")
    # # 将读取的数据转换为一维列表
    # cita = cita[1:].values.tolist()[0]
    # print(cita)
    answer = decrypt_query(cita, en_data)
    return answer

answer = query_answer()
print(answer)

