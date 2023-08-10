# -*- coding: utf-8 -*-
"""
@Author  : Morvan Li
@FileName: line_diagram.py
@Software: PyCharm
@Time    : 8/10/23 9:45 AM
"""
# import matplotlib.pyplot as plt
# import seaborn as sns
# import numpy as np
#
# # 创建一个2x3的子图布局
# fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(15, 10))
#
# # 生成x轴数据
# x = np.linspace(50, 10, 160)
#
# # 待设置的不同 y 轴标签
# y_labels = ['Y Label 1', 'Y Label 2', 'Y Label 3', 'Y Label 4', 'Y Label 5', 'Y Label 6']
#
# # 自定义的 y 值列表
# common_y_values = [6.067675, 6.067075, 6.067091, 6.067433, 6.067423, 6.068001, 6.067898, 6.067772, 6.068240, 6.068152,
#                    6.068186]
#
# # 循环绘制每个子图
# for i, row in enumerate(axes):
#     for j, ax in enumerate(row):
#         # 在当前子图上绘制三条线段，使用相同的 y 值列表
#         sns.lineplot(x=x, y=common_y_values, ax=ax, label='Line 1')
#         sns.lineplot(x=x, y=common_y_values, ax=ax, label='Line 2')
#         sns.lineplot(x=x, y=common_y_values, ax=ax, label='Line 3')
#
#         # 添加标题和标签
#         ax.set_title('Subplot Title')
#         ax.set_xlabel('X Label')
#
#         # 设置不同的 y 轴标签
#         ax.set_ylabel(y_labels[i * 3 + j])
#
#         # 添加图例并放置在右下角
#         ax.legend(loc='upper left', bbox_to_anchor=(1, 0))
#
# # 调整子图之间的间距
# plt.tight_layout()
#
# # 显示图形
# plt.show()

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from matplotlib.gridspec import GridSpec
from sklearn.preprocessing import StandardScaler, MinMaxScaler

scaler = MinMaxScaler()


# 定义移动平均函数
def moving_average(data, window_size):
    cumsum = np.cumsum(data)
    cumsum[window_size:] = cumsum[window_size:] - cumsum[:-window_size]
    return cumsum[window_size - 1:] / window_size


# 创建一个2x3的子图布局
fig = plt.figure(figsize=(16, 7))
gs = GridSpec(2, 3, figure=fig)

# 生成x轴数据
x = np.arange(50, 151, 20)  # 从50开始，到150结束，步长为10
x_label = np.arange(50, 151, 20)

# 绘制子图1
ax1 = fig.add_subplot(gs[0, 0])
y1 = scaler.fit_transform(np.array([6.0671, 6.0671, 6.0674, 6.0681, 6.0681, 6.0682]).reshape(-1, 1)).flatten()
y2 = scaler.fit_transform(np.array([5.572, 5.601, 5.635, 5.635, 5.634, 5.634]).reshape(-1, 1)).flatten()
y3 = scaler.fit_transform(np.array([6.036, 6.041, 6.045, 6.045, 6.047, 6.047]).reshape(-1, 1)).flatten()

sns.lineplot(x=x, y=y1, ax=ax1, marker='o', label='Lytro', linewidth=2, markersize=8)
sns.lineplot(x=x, y=y2, ax=ax1, marker='s', label='MFFW', linewidth=2, markersize=8)
sns.lineplot(x=x, y=y3, ax=ax1, marker='d', label='MFI-WHU', linewidth=2, markersize=8)
# ax1.set_title('Subplot 1 Title')
ax1.set_xlabel('X Label')
ax1.set_ylabel('MI')
ax1.set_xticks(x_label)  # 设置横坐标刻度
ax1.legend(loc='best')
plt.plot([110, 110, ], [0, 1.0, ], color='red',  linestyle='-.', alpha=0.3)
# 绘制子图2
ax2 = fig.add_subplot(gs[0, 1])
y4 = scaler.fit_transform(np.array([1.3855, 1.3858, 1.3859, 1.3861, 1.3861, 1.3862]).reshape(-1, 1)).flatten()
y5 = scaler.fit_transform(np.array([1.291, 1.291, 1.291, 1.291, 1.291, 1.291]).reshape(-1, 1)).flatten()
y6 = scaler.fit_transform(np.array([1.384, 1.385, 1.386, 1.387, 1.387, 1.387]).reshape(-1, 1)).flatten()
sns.lineplot(x=x, y=y4, ax=ax2, marker='o', label='Lytro', linewidth=2, markersize=8)
sns.lineplot(x=x, y=y5, ax=ax2, marker='s', label='MFFW', linewidth=2, markersize=8)
sns.lineplot(x=x, y=y6, ax=ax2, marker='d', label='MFI-WHU', linewidth=2, markersize=8)
ax2.set_xlabel('X Label')
ax2.set_ylabel('VIFF')
ax2.set_xticks(x_label)  # 设置横坐标刻度
ax2.legend(loc='best')
plt.plot([110, 110, ], [0, 1.0, ], color='red',  linestyle='-.', alpha=0.3)
# 绘制子图3
ax3 = fig.add_subplot(gs[0, 2])
y7 = scaler.fit_transform(np.array([0.7611, 0.7612, 0.7613, 0.7613, 0.7613, 0.7613]).reshape(-1, 1)).flatten()
y8 = scaler.fit_transform(np.array([0.7366, 0.7367, 0.7367, 0.7368, 0.7368, 0.7368]).reshape(-1, 1)).flatten()
y9 = scaler.fit_transform(np.array([0.7307, 0.7308, 0.7309, 0.7312, 0.7313, 0.7313]).reshape(-1, 1)).flatten()
sns.lineplot(x=x, y=y7, ax=ax3, marker='o', label='Lytro', linewidth=2, markersize=8)
sns.lineplot(x=x, y=y8, ax=ax3, marker='s', label='MFFW', linewidth=2, markersize=8)
sns.lineplot(x=x, y=y9, ax=ax3, marker='d', label='MFI-WHU', linewidth=2, markersize=8)
ax3.set_xlabel('X Label')
ax3.set_ylabel('Qabf')
ax3.set_xticks(x_label)  # 设置横坐标刻度
ax3.legend(loc='best')
plt.plot([110, 110, ], [0, 1.0, ], color='red',  linestyle='-.', alpha=0.3)
# 绘制子图4
ax4 = fig.add_subplot(gs[1, 0])
y10 = scaler.fit_transform(np.array([1.68307, 1.68307, 1.68310, 1.68310, 1.68310, 1.68310]).reshape(-1, 1)).flatten()
y11 = scaler.fit_transform(np.array([1.6411, 1.6412, 1.6412, 1.6412, 1.6412, 1.6412]).reshape(-1, 1)).flatten()
y12 = scaler.fit_transform(np.array([1.6908, 1.6909, 1.6910, 1.6910, 1.6910, 1.6910]).reshape(-1, 1)).flatten()
sns.lineplot(x=x, y=y10, ax=ax4, marker='o', label='Lytro', linewidth=2, markersize=8)
sns.lineplot(x=x, y=y11, ax=ax4, marker='s', label='MFFW', linewidth=2, markersize=8)
sns.lineplot(x=x, y=y12, ax=ax4, marker='d', label='MFI-WHU', linewidth=2, markersize=8)
ax4.set_xlabel('X Label')
ax4.set_ylabel('SSIM')
ax4.set_xticks(x_label)  # 设置横坐标刻度
ax4.legend(loc='best')
plt.plot([110, 110, ], [0, 1.0, ], color='red',  linestyle='-.', alpha=0.3)
# 绘制子图5
ax5 = fig.add_subplot(gs[1, 1])
y13 = scaler.fit_transform(np.array([7.5310, 7.5310, 7.5311, 7.5312, 7.5312, 7.5312]).reshape(-1, 1)).flatten()
y14 = scaler.fit_transform(np.array([7.158, 7.160, 7.162, 7.162, 7.162, 7.162]).reshape(-1, 1)).flatten()
y15 = scaler.fit_transform(np.array([7.313, 7.313, 7.313, 7.314, 7.314, 7.314]).reshape(-1, 1)).flatten()
sns.lineplot(x=x, y=y13, ax=ax5, marker='o', label='Lytro', linewidth=2, markersize=8)
sns.lineplot(x=x, y=y14, ax=ax5, marker='s', label='MFFW', linewidth=2, markersize=8)
sns.lineplot(x=x, y=y15, ax=ax5, marker='d', label='MFI-WHU', linewidth=2, markersize=8)
ax5.set_xlabel('X Label')
ax5.set_ylabel('QG')
ax5.set_xticks(x_label)  # 设置横坐标刻度
ax5.legend(loc='best')
plt.plot([110, 110, ], [0, 1.0, ], color='red',  linestyle='-.', alpha=0.3)
# 绘制子图6
ax6 = fig.add_subplot(gs[1, 2])
y16 = scaler.fit_transform(np.array([19.3047, 19.3052, 19.3056, 19.3061, 19.3059, 19.3058]).reshape(-1, 1)).flatten()
y17 = scaler.fit_transform(np.array([21.971, 21.971, 21.972, 21.972, 21.972, 21.972]).reshape(-1, 1)).flatten()
y18 = scaler.fit_transform(np.array([26.365, 26.373, 26.376, 26.391, 26.391, 26.393]).reshape(-1, 1)).flatten()
sns.lineplot(x=x, y=y16, ax=ax6, marker='o', label='Lytro', linewidth=2, markersize=8)
sns.lineplot(x=x, y=y17, ax=ax6, marker='>', label='MFFW', linewidth=2, markersize=8)
sns.lineplot(x=x, y=y18, ax=ax6, marker='d', label='MFI-WHU', linewidth=2, markersize=8)
ax6.set_xlabel('X Label')
ax6.set_ylabel('QCB')
ax6.set_xticks(x_label)  # 设置横坐标刻度
ax6.legend(loc='best')
plt.plot([110, 110, ], [0, 1.0, ], color='red',  linestyle='-.', alpha=0.3)
# 调整布局
plt.tight_layout()

# 显示图形
plt.show()

# import matplotlib.pyplot as plt
#
# # 数据
# x = [1, 2, 3, 4, 5, 6]  # 数据点
# y1 = [6.0671, 6.0671, 6.0674, 6.0681, 6.0681, 6.0682]
# y2 = [5.572, 5.601, 5.635, 5.635, 5.634, 5.634]
# y3 = [6.036, 6.041, 6.045, 6.045, 6.047, 6.047]
#
# # 绘制折线图
# plt.figure(figsize=(8, 6))
# plt.plot(x, y1, marker='o', label='Method 1')
# plt.plot(x, y2, marker='s', label='Method 2')
# plt.plot(x, y3, marker='d', label='Method 3')
#
# plt.title('Comparison of Methods on MI Metric')
# plt.xlabel('Data Point')
# plt.ylabel('MI Metric Value')
# plt.xticks(x)
# plt.legend()
# plt.grid(True)
#
# plt.show()
