'''

CS1 generate the function key for CS2

'''
from TA import total_samples, public_key, SKGenerate
import numpy as np
import pandas as pd

num = total_samples()
d = 7

cita = np.zeros(d+1, dtype=int)
cita = np.append(cita, -1)

def deliever_cita():
    return cita
def get_skf():
    return SKGenerate(cita)