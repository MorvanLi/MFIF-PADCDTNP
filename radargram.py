# -*- coding: utf-8 -*-
# @Time    : 2023/7/26 21:43
# @Author  : Li Bo
# @FileName: leidatu.py
# @Software: PyCharm

# import pandas as pd
# import numpy as np
# from sklearn.preprocessing import MinMaxScaler, StandardScaler
# import matplotlib.pyplot as plt
# # 假设有多个算法的性能数据，其中自己的算法优于其他算法
# with plt.style.context(['science', 'grid']):
#     algorithm_names = ['SF', 'EOG', 'MSMFM', 'EOL', 'SML', 'SML+EOL']
#     performance_data = {
#         'SSIM': [0.8415, 0.8410, 0.8416, 0.8395, 0.8421, 0.8417],  # 各个算法在Metric1上的性能数据
#         'FMI': [0.5960, 0.6029, 0.5953, 0.5581, 0.5968, 0.5990],  # 各个算法在Metric2上的性能数据
#         'Qabf': [0.7163, 0.6430, 0.7550, 0.7511, 0.7328, 0.7619],  # 各个算法在Metric2上的性能数据
#         '$Q_{MI}$': [1.1707, 1.1503, 1.1668, 1.1333, 1.1707, 1.1716],  # 各个算法在Metric2上的性能数据
#         '$Q_{S}$': [0.9148, 0.8826, 0.9425, 0.9437, 0.9287, 0.9458],  # 各个算法在Metric2上的性能数据
#         '$Q_{CB}$': [0.7661, 0.7552, 0.7979, 0.7960, 0.7877, 0.8107],  # 各个算法在Metric2上的性能数据
#         '$Q_G$': [0.6751, 0.6498, 0.7060, 0.7087, 0.6914, 0.7256],  # 各个算法在Metric2上的性能数据
#         'Nabf': [0.0001, 0.0001, 0.0002, 0.0070, 0.0003, 0.0002],  # 各个算法在Metric2上的性能数据
#
#     }
#
#     # 创建数据框
#     df = pd.DataFrame(performance_data, index=algorithm_names)
#
#     # 归一化处理
#     scaler = MinMaxScaler(feature_range=(0.1, 1))
#     df_normalized = pd.DataFrame(scaler.fit_transform(df), columns=df.columns, index=df.index)
#
#     # 计算雷达图中的角度
#     angles = np.linspace(0, 2 * np.pi, num=8, endpoint=False).tolist()
#     angles += angles[:1]  # 闭合雷达图
#
#     # 创建子图和坐标轴
#     fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
#
#     # colors = ['#4C72B0', '#DD8452', '#55A868', '#8172B3']  # 设置线段的颜色
#     # linewidths = [2, 2, 2, 2]  # 设置线段的粗细
#     # 绘制每个算法的雷达图
#     for i in range(len(algorithm_names)):
#         values = df_normalized.iloc[i].tolist()
#         values += values[:1]  # 闭合多边形
#         ax.plot(angles, values, label=algorithm_names[i], linewidth=2)
#         ax.fill(angles, values, alpha=0.2)  # 设置填充颜色
#
#     # 设置刻度标签
#     ax.set_xticks(angles[:-1])
#     ax.set_xticklabels(df.columns)
#
#     # 添加网格线
#     ax.yaxis.grid(True)
#
#     # 添加图例
#     plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))
#
#     # 添加标题
#     # plt.title('Normalized Performance Comparison of Algorithms')
#     plt.tight_layout()
#     # 显示图形
#     plt.savefig("1111.pdf", dpi=300, format="pdf", bbox_inches="tight")
#     # 显示图表
#     plt.show()


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

# Rest of your code (omitted for brevity)
with plt.style.context(['science', 'grid']):
    algorithm_names = ['SF', 'EOG', 'MSMFM', 'EOL', 'SML', 'SML+EOL']
    performance_data = {
        'SSIM': [0.8415, 0.8410, 0.8416, 0.8395, 0.8421, 0.8417],  # 各个算法在Metric1上的性能数据
        'FMI': [0.5960, 0.6029, 0.5953, 0.5581, 0.5968, 0.5990],  # 各个算法在Metric2上的性能数据
        'Qabf': [0.7163, 0.6430, 0.7550, 0.7511, 0.7328, 0.7619],  # 各个算法在Metric2上的性能数据
        '$Q_{MI}$': [1.1707, 1.1503, 1.1668, 1.1333, 1.1707, 1.1716],  # 各个算法在Metric2上的性能数据
        '$Q_{S}$': [0.9148, 0.8826, 0.9425, 0.9437, 0.9287, 0.9458],  # 各个算法在Metric2上的性能数据
        '$Q_{CB}$': [0.7661, 0.7552, 0.7979, 0.7960, 0.7877, 0.8107],  # 各个算法在Metric2上的性能数据
        '$Q_G$': [0.6751, 0.6498, 0.7060, 0.7087, 0.6914, 0.7256],  # 各个算法在Metric2上的性能数据
        'Nabf': [0.0001, 0.0001, 0.0002, 0.0070, 0.0003, 0.0002],  # 各个算法在Metric2上的性能数据

    }

    # 创建数据框
    df = pd.DataFrame(performance_data, index=algorithm_names)

    # 归一化处理
    scaler = MinMaxScaler(feature_range=(0.1, 1))
    df_normalized = pd.DataFrame(scaler.fit_transform(df), columns=df.columns, index=df.index)

    # 计算雷达图中的角度
    angles = np.linspace(0, 2 * np.pi, num=8, endpoint=False).tolist()
    angles += angles[:1]  # 闭合雷达图
    # Create two radar charts side by side
    fig, axs = plt.subplots(1, 2, figsize=(16, 8), subplot_kw=dict(polar=True))

    # Loop through each subplot (axis) and plot the radar chart
    for ax in axs:
        # Rest of your code for radar chart (omitted for brevity)

        # Plot each algorithm's radar chart on the corresponding axis
        for i in range(len(algorithm_names)):
            values = df_normalized.iloc[i].tolist()
            values += values[:1]  # 闭合多边形
            ax.plot(angles, values, label=algorithm_names[i], linewidth=2)
            ax.fill(angles, values, alpha=0.2)  # 设置填充颜色
            ax.set_xticks(angles[:-1])
            ax.set_xticklabels(df.columns)
        # Rest of your code for radar chart (omitted for brevity)

    # Add titles to each subplot
    axs[0].set_title('Dataset: Lytro')
    axs[1].set_title('Dataset: MFFW')

    # Show the legend outside of the plots
    # axs[0].legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))
    axs[1].legend(loc='lower right', bbox_to_anchor=(0.01, 0.1))
    # Adjust layout and spacing
    plt.tight_layout()

    # Save the figure to a file
    # plt.savefig("radar_charts.pdf", dpi=300, format="pdf", bbox_inches="tight")

    # Show the plot
    plt.show()
