"""

each dataowners first preprocess its local dataset

"""

import pandas as pd
import numpy as np
import random

# 假设有两个用户DO1, DO2
def get_data():
    data = pd.read_csv('../datasets/winequality-red.csv', sep=';')
    return data


def get_MaxMinN(X):
    X_max = []
    X_min = []
    n = []
    for column in X.columns:
        max = np.max(X[column])
        min = np.min(X[column])
        _n = len(X[column])
        X_max.append(max)
        X_min.append(min)
        n.append(_n)
    return X_max, X_min, n

def seperate_data():
    data = get_data()
    n = random.randint(data.shape(1))
    X1 = data.iloc[:n, :-1]
    y1 = data.iloc[:n, -1]
    X2 = data.iloc[n:, :-1]
    y2 = data.iloc[n:, -1]
    return X1, y1, X2, y2