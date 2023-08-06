#!/usr/bin/env python
# coding=utf-8
'''
brief        :  
Author       : knightdby knightdby@163.com
Date         : 2023-02-24 16:57:43
FilePath     : /wheel/manifast/iostream.py
Description  : 
LastEditTime : 2023-02-24 17:49:03
LastEditors  : knightdby
Copyright (c) 2023 by Inc, All Rights Reserved.
'''

import os
import cv2
import yaml
import json
import numpy as np


def getAllFile(file_dir='', tail_name=['.jpg'], filter='.'):
    """
     description: 获取指定文件夹下的所有指定文件类型的文件，到List
     param       {*} file_dir  指定的迭代检索的文件夹
     param       {*} tail_name 迭代检测的文件类型
     return      {*} 包含所有文件绝对路径的list
    """
    L = []
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] in tail_name and filter in os.path.join(root, file):
                L.append(os.path.join(root, file))
    return L


def writeToJson(data={}, save_path='./results.json'):
    """
     description: 将data保存到指定的json文件下
     param       {*} data 
     param       {*} save_path
     return      {*}
    """
    with open(save_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)


def readFromJson(readPath):
    with open(readPath, "r", encoding='utf-8') as f:
        dict = json.load(f)
    # print(dics)
    return dict


def readFromTxt(txt_path):
    constants = []
    with open(txt_path, 'r') as file_to_read:
        while True:
            lines = file_to_read.readline()  # 整行读取数据
            if not lines:
                break
            # 将整行数据分割处理，如果分割符是空格，括号里就不用传入参数，如果是逗号， 则传入‘，'字符。
            # p_tmp = [i for i in lines.split(' ')]

            constants.append(lines.strip('\n'))  # 添加新读取的数据
            # Efield.append(E_tmp)
            pass
    return constants


def writeToTxt(data=[], save_path='./results.txt'):
    """
     description: 将data保存到指定的json文件下
     param       {*} data 
     param       {*} save_path
     return      {*}
    """
    with open(save_path, 'w') as f:
        pass
    for file in data:
        with open(save_path, 'a') as f:
            f.write(file+'\n')


def loadImg(fp):
    img = cv2.imread(fp, cv2.IMREAD_UNCHANGED)
    if img.ndim == 3:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img


def plusImgMask(img, mask):
    """
     description: 叠加彩色图像与mask
     param       {*} img h*w*c
     param       {*} mask h*w
     return      {*}
    """
    if mask.ndim == 3:
        mask = mask.squeeze()  # 去掉batch維度
    mask = mask.astype(np.uint8)
    display_mask = np.zeros_like(img)
    display_mask[mask == 1, 0] = 255
    masked = cv2.add(img, np.zeros(
        np.shape(img), dtype=np.uint8), mask=mask)
    masked = cv2.addWeighted(img, 0.5, display_mask, 0.5, 0)
    return masked
