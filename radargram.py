# -*- coding: utf-8 -*-
# @Time    : 2023/7/26 21:43
# @Author  : Li Bo
# @FileName: leidatu.py
# @Software: PyCharm

from typing import List

import matplotlib.pyplot as plt
import numpy as np

with plt.style.context(['science']):
    algorithm_names = ['SF', 'EOG', 'MSMFM', 'EOL', 'SML', 'SML+EOL']
    results = [{"SSIM": 87, "$FMI_{w}$": 79, "Qabf": 95, "$Q_{MI}$": 92, "$Q_{S}$": 85, "$Q_{CB}$": 86, "$Q_G$": 86},
               {"大学英语": 80, "高等数学": 90, "体育": 91, "计算机基础": 85, "程序设计": 88, "程序": 87, "序": 86}]
    data_length = len(results[0])
    angles = np.linspace(0, 2 * np.pi, data_length, endpoint=False)
    labels = [key for key in results[0].keys()]
    score = [[v for v in result.values()] for result in results]

    score_a = [[0.8153846153846303, 0.8767857142857132, 0.6931875525651812, 0.9812010443864239, 0.6075949367088587,
                0.3571171171171166, 0.4670184696569919, 0.8153846153846303],
               [0.6615384615384414, 1.0, 0.20000000000000018, 0.5550913838120124, 0.1999999999999993,
                0.1999999999999993,
                0.20000000000000018, 0.6615384615384414],
               [0.846153846153868, 0.8642857142857157, 0.9535744322960475, 0.8997389033942582, 0.9582278481012647,
                0.8154954954954956, 0.7931398416886539, 0.846153846153868],
               [0.19999999999998863, 0.1999999999999993, 0.927333894028596, 0.1999999999999993, 0.9734177215189863,
                0.7881081081081085, 0.8216358839050129, 0.19999999999998863],
               [1.0, 0.8910714285714292, 0.804205214465938, 0.9812010443864239, 0.7835443037974663, 0.6684684684684683,
                0.6390501319261208, 1.0],
               [0.8769230769231058, 0.930357142857142, 1.0000000000000009, 1.0, 0.9999999999999982, 1.0, 1.0,
                0.8769230769231058]]

    score_b = [[0.9737226277372244, 0.9880553532410778, 0.7159678858162364, 0.888734602463606, 0.1999999999999993,
                0.8509539842873179, 0.7877073170731708, 0.9737226277372244],
               [0.991240875912407, 0.9822286962855062, 0.5853702051739527, 1.0, 0.4520900321543415, 0.8716049382716058,
                0.8907317073170733, 0.991240875912407],
               [0.9737226277372244, 0.9927166788055355, 1.0000000000000009, 0.9007390817469205, 0.9948553054662383,
                0.8967452300785643, 0.9711219512195124, 0.9737226277372244],
               [0.1999999999999993, 0.19999999999999996, 0.20000000000000018, 0.19999999999999996, 0.23858520900321523,
                0.20000000000000018, 0.19999999999999996, 0.1999999999999993],
               [0.9883211678832069, 0.9985433357611071, 0.838001784121321, 0.9163269876819711, 0.7736334405144696,
                0.8985409652076326, 0.9438048780487807, 0.9883211678832069],
               [1.0, 1.0, 0.9743086529884044, 0.9174020156774918, 1.0, 1.0, 1.0000000000000002, 1.0]]
    angles = np.concatenate((angles, [angles[0]]))
    labels = np.concatenate((labels, [labels[0]]))
    fig = plt.figure(figsize=(12, 6))
    # fig.suptitle("计算机专业大一（上）")
    ax1 = plt.subplot(121, polar=True)
    ax2 = plt.subplot(122, polar=True)
    ax, data, name = [ax1, ax2], [score_a, score_b], ["Dataset: Lytro", "Dataset: MFFW"]
    cors = ['#817B84', '#8E5C41', '#966AB9', '#2BA32A', '#D52A2D',  '#FF9A3D']
    for i in range(2):
        for j in np.arange(0, 1 + 0.2, 0.2):
            ax[i].plot(angles, 8 * [j], '--', lw=0.5, color='black')
        for j in range(7):
            ax[i].plot([angles[j], angles[j]], [0, 1], '-', lw=0.5, color='gray')
        for num in range(6):
            ax[i].plot(angles, data[i][num], lw=1.5, label=algorithm_names[num], color=cors[num])
            # 隐藏最外圈的圆
            ax[i].spines['polar'].set_visible(False)
            # 隐藏圆形网格线
            ax[i].grid(False)
            # for a, b in zip(angles, data[i]):
            #     ax[i].text(a, b+5, '%.00f' % b, ha='center', va='center', fontsize=12, color='b')
            ax[i].fill(angles, data[i][num], alpha=0.1)  # 设置填充颜色
            ax[i].set_thetagrids(angles * 180 / np.pi, labels)
            ax[i].set_theta_zero_location('N')
            ax[i].set_rlim(0, 1)
            ax[i].set_rlabel_position(30)
            ax[i].set_title(name[i])


    # leg = ax[1].legend(loc='lower center', bbox_to_anchor=(0.001, 0.15), )
    #
    # # 设置图例里线段的宽度
    # for legobj in ax[1].legend().legendHandles:
    #     legobj.set_linewidth(5)

    leg = ax[1].legend(loc='lower left', frameon=True, bbox_to_anchor=(-0.25, -0.06))

    # 将图例显示在最底层
    leg.set_zorder(0.001)
    for legobj in leg.legendHandles:
        legobj.set_linewidth(5)  # 设置线段的宽度为3
    plt.savefig("radar_charts.pdf", dpi=300, format="pdf", bbox_inches="tight")
    plt.show()

