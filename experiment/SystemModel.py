from DOs import *

data = get_total_data()
X, y = simulate_multiusers(data, 2)
X_Max, X_Min, N = get_MaxMinN(X)
print(X_Max, X_Min, N)

from TA import XMax_Xmin, total_samples
g_max, g_min = XMax_Xmin(X_Max, X_Min, N)
g_n = total_samples(N)

X = normalize_global(X, g_max, g_min)
M = extend_to_matrix(X)
print('---------before encrypted----------')
print(M)
M = encrypt_data(M)
print('---------after encrypted----------')
print(M)


