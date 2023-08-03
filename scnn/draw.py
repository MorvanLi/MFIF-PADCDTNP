# -*- coding: utf-8 -*-
"""
@Author  : Morvan Li
@FileName: draw.py
@Software: PyCharm
@Time    : 8/3/23 3:19 PM
"""
from typing import List
import logging
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from scnn import setup_logger

logger = logging.getLogger('scnn')

class RadarChartPlotter:
    def __init__(self, results, score_a, score_b, score_c):
        self.algorithm_names = ['SF', 'EOG', 'MSMFM', 'EOL', 'SML', 'SML+EOL']
        self.data_length = len(results[0])
        self.angles = np.linspace(0, 2 * np.pi, self.data_length, endpoint=False)
        self.labels = [key for key in results[0].keys()]
        self.score = [[v for v in result.values()] for result in results]
        self.score_a = score_a
        self.score_b = score_b
        self.score_c = score_c

    def plot_radar_charts(self):
        self.angles = np.concatenate((self.angles, [self.angles[0]]))
        self.labels = np.concatenate((self.labels, [self.labels[0]]))

        fig = plt.figure(figsize=(18, 6))
        ax1 = plt.subplot(131, polar=True)
        ax2 = plt.subplot(132, polar=True)
        ax3 = plt.subplot(133, polar=True)
        ax_list = [ax1, ax2, ax3]

        data_list = [self.score_a, self.score_b, self.score_c]
        name_list = ["Dataset: Lytro", "Dataset: MFFW", "Dataset: MFI-WHU"]
        cors = ['#817B84', '#8E5C41', '#966AB9', '#2BA32A', '#D52A2D', '#FF9A3D']

        for i, ax in enumerate(ax_list):
            for j in np.arange(0, 1 + 0.2, 0.2):
                ax.plot(self.angles, 8 * [j], '--', lw=0.5, color='black') # 设置为8是为了重合起点和终点
            for j in range(7):
                ax.plot([self.angles[j], self.angles[j]], [0, 1], '-', lw=0.5, color='gray')
            for num in range(6):
                ax.plot(self.angles, data_list[i][num], lw=1.5, label=self.algorithm_names[num], color=cors[num])
                ax.spines['polar'].set_visible(False)
                ax.grid(False)
                ax.fill(self.angles, data_list[i][num], alpha=0.1)
                ax.set_thetagrids(self.angles * 180 / np.pi, self.labels)
                ax.set_theta_zero_location('N')
                ax.set_rlim(0, 1)
                ax.set_rlabel_position(30)
                ax.set_title(name_list[i])

        # Add legend
        leg = ax.legend(loc='best', bbox_to_anchor=(1.4, 0.7))
        # Move the legend to the bottom layer
        # leg.set_zorder(0.001)
        for legobj in leg.legendHandles:
            legobj.set_linewidth(8)

        plt.savefig("radar_charts.pdf", dpi=300, format="pdf", bbox_inches="tight")
        logger.info("Save Image Successful")
        plt.show()


# Example usage:

if __name__ == '__main__':
    # setup_logger()
    logger.info("Start processing data")

    results = [{"SSIM": 87, "$FMI_{w}$": 79, "Qabf": 95, "$Q_{MI}$": 92, "$Q_{S}$": 85, "$Q_{CB}$": 86, "$Q_G$": 86}]

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

    plotter = RadarChartPlotter(results, score_a, score_b, score_b)
    plotter.plot_radar_charts()

