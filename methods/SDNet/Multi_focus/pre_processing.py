# -*- coding: utf-8 -*-
"""
@Author  : Morvan Li
@FileName: pre_processing.py
@Software: PyCharm
@Time    : 8/2/23 11:14 AM
"""

import os
from shutil import copy, rmtree

import cv2
import numpy as np
from PIL import Image
import shutil

def list_files_in_directory(directory):
    mk_file(directory + 'source1')
    mk_file(directory + 'source2')
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if 'A' in file_path.split('/')[-1]:
                shutil.move(file_path, directory + 'source1')
            else:
                shutil.move(file_path, directory + 'source2')



# 　first
def first():
    for num in range(1, 21):
        I_under = Image.open(f"/home/synsense-1/LIBO/MFIF-PADCDTNP/Lytro/source_1/{num}.jpg")
        Y_under, _, _ = I_under.convert("YCbCr").split()
        Y_under.save(f"./Test_far/{num}.jpg")

        I_over = Image.open(f"/home/synsense-1/LIBO/MFIF-PADCDTNP/Lytro/source_2/{num}.jpg")
        Y_over, _, _ = I_over.convert("YCbCr").split()
        Y_over.save(f"Test_near/{num}.jpg")


def mk_file(file_path: str):
    if os.path.exists(file_path):
        # 如果文件夹存在，则先删除原文件夹在重新创建
        rmtree(file_path)
    os.makedirs(file_path)


def rgb_to_ycbcr(img_rgb):
    R = img_rgb[:, :, 0]
    G = img_rgb[:, :, 1]
    B = img_rgb[:, :, 2]

    Y = 0.257 * R + 0.504 * G + 0.098 * B + 16
    Cb = -0.148 * R - 0.291 * G + 0.439 * B + 128
    Cr = 0.439 * R - 0.368 * G - 0.071 * B + 128

    return Y, Cb, Cr


def ycbcr_to_rgb(img_ycbcr):
    Y = img_ycbcr[:, :, 0]
    Cb = img_ycbcr[:, :, 1]
    Cr = img_ycbcr[:, :, 2]

    R = 1.164 * (Y - 16) + 1.596 * (Cr - 128)
    G = 1.164 * (Y - 16) - 0.392 * (Cb - 128) - 0.813 * (Cr - 128)
    B = 1.164 * (Y - 16) + 2.017 * (Cb - 128)

    image_rgb = np.stack([R, G, B], axis=-1)
    return image_rgb


def last():
    mk_file('./result/SDNet-Lytro/')
    for i in range(1, 21):
        I_result = cv2.imread(f'./result/epoch19/{i}.jpg', cv2.IMREAD_GRAYSCALE).astype(np.double)
        I_init_under = cv2.imread(f'/home/synsense-1/LIBO/MFIF-PADCDTNP/Lytro/source_1/{i}.jpg').astype(np.double)
        I_init_over = cv2.imread(f'/home/synsense-1/LIBO/MFIF-PADCDTNP/Lytro/source_2/{i}.jpg').astype(np.double)

        Y1, Cb1, Cr1 = rgb_to_ycbcr(I_init_under)
        Y2, Cb2, Cr2 = rgb_to_ycbcr(I_init_over)

        H, W = Cb1.shape
        Cb = np.ones([H, W])
        Cr = np.ones([H, W])
        for k in range(H):
            for n in range(W):
                if abs(Cb1[k, n] - 128) == 0 and abs(Cb2[k, n] - 128) == 0:
                    Cb[k, n] = 128
                else:
                    middle_1 = Cb1[k, n] * abs(Cb1[k, n] - 128) + Cb2[k, n] * abs(Cb2[k, n] - 128)
                    middle_2 = abs(Cb1[k, n] - 128) + abs(Cb2[k, n] - 128)
                    Cb[k, n] = middle_1 / middle_2

                if abs(Cr1[k, n] - 128) == 0 and abs(Cr2[k, n] - 128) == 0:
                    Cr[k, n] = 128
                else:
                    middle_3 = Cr1[k, n] * abs(Cr1[k, n] - 128) + Cr2[k, n] * abs(Cr2[k, n] - 128)
                    middle_4 = abs(Cr1[k, n] - 128) + abs(Cr2[k, n] - 128)
                    Cr[k, n] = middle_3 / middle_4

        I_final_YCbCr = np.stack([I_result, Cb, Cr], axis=-1)
        I_final_RGB = ycbcr_to_rgb(I_final_YCbCr)
        I_final_RGB = np.clip(I_final_RGB, 0, 255).astype(np.uint8)

        cv2.imwrite(f'./result/SDNet-Lytro/{i}.png', I_final_RGB)


if __name__ == '__main__':
    # list_files_in_directory('/home/synsense-1/LIBO/MFIF-PADCDTNP/Lytro')
    # first()
    last()