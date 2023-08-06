#!/usr/bin/env python
# coding=utf-8
'''
brief        :  
Author       : knightdby knightdby@163.com
Date         : 2023-02-24 18:22:41
FilePath     : /wheel/manifast/import_pkg.py
Description  : 
LastEditTime : 2023-02-24 18:36:35
LastEditors  : knightdby
Copyright (c) 2023 by Inc, All Rights Reserved.
'''

import os
import cv2
import sys
import json
import random
import shutil
import matplotlib
import numpy as np
import pandas as pd
from .iostream import *
from glob import glob
from tqdm import tqdm
from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
from easydict import EasyDict as edict
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
if not os.getcwd().split('\\')[-1].find('notebooks') == -1:
    os.chdir('../')
sys.path.append(os.getcwd())
