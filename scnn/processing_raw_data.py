# -*- coding: utf-8 -*-
"""
@Author  : Morvan Li
@FileName: tt.py
@Software: PyCharm
@Time    : 7/27/23 2:26 PM
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

algorithm_names = ['SF', 'EOG', 'MSMFM', 'EOL', 'SML', 'SML+EOL']
performance_data_lytro = {
    'SSIM': [0.8415, 0.8410, 0.8416, 0.8395, 0.8421, 0.8417],  # 各个算法在Metric1上的性能数据
    'FMI': [0.5960, 0.6029, 0.5953, 0.5581, 0.5968, 0.5990],  # 各个算法在Metric2上的性能数据
    'Qabf': [0.7163, 0.6430, 0.7550, 0.7511, 0.7328, 0.7619],  # 各个算法在Metric2上的性能数据
    'QMI': [1.1707, 1.1503, 1.1668, 1.1333, 1.1707, 1.1716],  # 各个算法在Metric2上的性能数据
    'QS': [0.9148, 0.8826, 0.9425, 0.9437, 0.9287, 0.9458],  # 各个算法在Metric2上的性能数据
    'QCB': [0.7661, 0.7552, 0.7979, 0.7960, 0.7877, 0.8107],  # 各个算法在Metric2上的性能数据
    'QG': [0.6751, 0.6498, 0.7060, 0.7087, 0.6914, 0.7256],  # 各个算法在Metric2上的性能数据
    # 'Nabf': [0.0002, 0.0003, 0.0003, 0.0070, 0.0003, 0.0002],  # 各个算法在Metric2上的性能数据

}

performance_data_mffw = {
    'SSIM': [0.8215, 0.8221, 0.8215, 0.7950, 0.8220, 0.8224],  # 各个算法在Metric1上的性能数据
    'FMI': [0.5726, 0.5706, 0.5742, 0.3021, 0.5762, 0.5767],  # 各个算法在Metric2上的性能数据
    'Qabf': [0.7005, 0.6822, 0.7403, 0.6282, 0.7176, 0.7367],  # 各个算法在Metric2上的性能数据
    'QMI': [1.1281, 1.1902, 1.1348, 0.7437, 1.1435, 1.1441],  # 各个算法在Metric2上的性能数据
    'QS': [0.8931, 0.9029, 0.9240, 0.8946, 0.9154, 0.9242],  # 各个算法在Metric2上的性能数据
    'QCB': [0.7408, 0.7431, 0.7459, 0.6683, 0.7461, 0.7574],  # 各个算法在Metric2上的性能数据
    'QG': [0.6475, 0.6739, 0.6945, 0.4969, 0.6875, 0.7019],  # 各个算法在Metric2上的性能数据
    # 'Nabf': [0.0005, 0.0005, 0.0007, 0.03, 0.0004, 0.0004],  # 各个算法在Metric2上的性能数据

}

# 创建数据框
df_lytro = pd.DataFrame(performance_data_lytro, index=algorithm_names)
df_mffw = pd.DataFrame(performance_data_mffw, index=algorithm_names)

# 归一化处理
scaler = MinMaxScaler(feature_range=(0.2, 1))
df_lytro_normalized = pd.DataFrame(scaler.fit_transform(df_lytro), columns=df_lytro.columns, index=df_lytro.index)
df_mffw_normalized = pd.DataFrame(scaler.fit_transform(df_mffw), columns=df_mffw.columns, index=df_mffw.index)

# Iterate through each row of the DataFrame
print(performance_data_mffw)
print("*" * 50)
score_a = []

for index, row in df_lytro_normalized.iterrows():
    tmp = []
    tmp.append(row['SSIM'])
    tmp.append(row['FMI'])
    tmp.append(row['Qabf'])
    tmp.append(row['QMI'])
    tmp.append(row['QS'])
    tmp.append(row['QCB'])
    tmp.append(row['QG'])
    score_a.append(tmp)

print(score_a)