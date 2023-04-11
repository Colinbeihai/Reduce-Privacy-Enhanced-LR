from DOs import *
from TA import *

def normalize_global():
    X, _ = seperate_data()
    # print(f'before glo_norm{X}')
    g_max, g_min = XMax_Xmin()
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

pk = public_key()
X_gnorm = normalize_global()
for X_i in X_gnorm:
    for i in range(len(X_i)):
        en_X = TA.encrypt(pk, X_i.iloc[i])
        X_i.iloc[i] = en_X
