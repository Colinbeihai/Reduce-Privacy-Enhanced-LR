# 非交互的隐私保护线性回归算法

## paillier加密 密文训练

### 一种基于密文训练的联邦学习线性回归算法

![image](https://github.com/user-attachments/assets/df548be2-a34f-447b-b903-df8a38225375)



### 如何使用
程序入口在 experiment/**SystemModel.py**，项目框架图为

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

### 方案对比

在确保数据隐私的情况下，计算时间和通信开销在多个数据集上的表现都有显著提升

![image](https://github.com/user-attachments/assets/8828e3e1-587a-404b-92c4-f354bfb8b30a)

