# 非交互的隐私保护线性回归算法

### 一种基于密文训练的联邦学习线性回归模型
算法示意图
![image](https://github.com/user-attachments/assets/bf898dd2-ac5e-4ad3-bd38-4e797ac1a583)


### 如何使用
程序入口在 experiment/SystemModel.py，项目框架图为
project/
├── crypto/
│   ├── paillier_FE.py    <--paillier加密算法
├── dataset/              <--数据集
├── experiment/
│   ├── CS.py             <--云服务器，负责对数据聚合，训练模型
│   ├── DOs.py             <--数据所有者，负责对数据加密，上传
│   ├── QU.py             <--数据查询者，上传密文数据，得到预测值
│   ├── SystemModel.py     <-- ！程序入口
│   └── TA.py             <--可信机构，负责生成分发秘钥
├── parameter/
│   ├── cita.csv         <--供存储模型参数
└── utils.py             <--密码学相关工具
