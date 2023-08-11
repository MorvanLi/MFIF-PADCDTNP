# -*- coding: utf-8 -*-
"""
@Author  : Morvan Li
@FileName: eval.py
@Software: PyCharm
@Time    : 7/18/23 5:46 PM
"""

from scnn.Evaluator import Evaluator

from scnn.img_read_save import img_save, image_read_cv2
import warnings
import logging


warnings.filterwarnings("ignore")
logging.basicConfig(level=logging.CRITICAL)

import os
import numpy as np
import pandas as pd

# names = ['BF-WHU', 'CNN-WHU', 'MFF-GAN-WHU', 'SDNet-WHU', 'SESF-WHU', 'SwinFusion-WHU',
#          'U2Fusion-WHU', 'ZMFF-WHU', 'Proposed-WHU']
#
# # 定义指标名称
# metrics = ['MI', 'VIFF', 'Qabf', 'SSIM', 'QG', 'QCB', ]
#
# # 创建空的DataFrame用于保存数据
# df = pd.DataFrame(columns=metrics, index=names)
#
# for alg in names:
#     ori_img_folder = os.path.join('/home/synsense-1/LIBO/MFIF-PADCDTNP/datasets/', 'MFI-WHU')
#     eval_folder = os.path.join('/home/synsense-1/LIBO/MFIF-PADCDTNP/results/WHU/', alg)
#     metric_result = np.zeros((6))
#     for img_name in os.listdir(os.path.join(ori_img_folder, "source_1")):
#         ir = image_read_cv2(os.path.join(ori_img_folder, "source_1", img_name), 'GRAY')
#         vi = image_read_cv2(os.path.join(ori_img_folder, "source_2", img_name), 'GRAY')
#         fi = image_read_cv2(os.path.join(eval_folder, img_name.split('.')[0] + ".png"), 'GRAY')
#         metric_result += np.array([
#             Evaluator.MI(fi, ir, vi), Evaluator.VIFF(fi, ir, vi), Evaluator.Qabf(fi, ir, vi),
#             Evaluator.SSIM(fi, ir, vi),
#             Evaluator.EN(fi),
#             Evaluator.SF(fi), ])
#
#     metric_result /= len(os.listdir(eval_folder))
#
#     # 将metric_result保存到DataFrame中
#     df.loc[alg] = metric_result
#
# # 将DataFrame保存到Excel文件中
# output_file = './WHU.xlsx'
# df.to_excel(output_file)


# eval_folder = os.path.join('/home/synsense-1/LIBO/MFIF-PADCDTNP/results/Lytro/', 'CNN-Lytro')
# ori_img_folder = os.path.join('/home/synsense-1/LIBO/MFIF-PADCDTNP/datasets/', 'Lytro')
#
# metric_result = np.zeros((6))
# for img_name in os.listdir(os.path.join(ori_img_folder, "source_1")):
#     ir = image_read_cv2(os.path.join(ori_img_folder, "source_1", img_name), 'GRAY')
#     vi = image_read_cv2(os.path.join(ori_img_folder, "source_2", img_name), 'GRAY')
#     fi = image_read_cv2(os.path.join(eval_folder, img_name.split('.')[0] + ".png"), 'GRAY')
#     metric_result += np.array([Evaluator.EN(fi), Evaluator.MSE(fi, ir, vi),
#                                Evaluator.MI(fi, ir, vi), Evaluator.VIFF(fi, ir, vi)
#                                   , Evaluator.Qabf(fi, ir, vi), Evaluator.SSIM(fi, ir, vi)])
#
# metric_result /= len(os.listdir(eval_folder))
#
# print(metric_result)