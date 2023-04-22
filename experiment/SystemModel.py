from DOs import DataOwners
from TA import TrustedAuthority
from CS import CloudSever

if __name__=='__main__':
    # 用户上传本地最大最小值
    DOs = DataOwners()
    data = DOs.get_total_data(DOs.data_path)
    X, y = DOs.simulate_multiusers(data, 2)
    X_Max, X_Min, N = DOs.get_MaxMinN(X)
    print(N)

    # 全局归一化，并加密本地数据
    d = 10
    eta = d + 2
    sec_param = 1024

    TA = TrustedAuthority(eta, sec_param)
    pk = TA.public_key()
    g_max, g_min = TA.XMax_Xmin(X_Max, X_Min, N)
    g_n = TA.total_samples(N)
    X = DOs.normalize_global(X, g_max, g_min)
    M = DOs.extend_to_matrix(X)
    M = DOs.encrypt_data(M, pk)

    CS = CloudSever(g_n, d)
    agg_M = CS.re_aggregation(M)
    CS.iterration_updata(agg_M, TA)


