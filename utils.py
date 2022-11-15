import numpy as np
from dtw01 import *
import math
import re
#y是x的子序列，从x的第三个数字开始一一匹配

def xy_right_sin(x, y):
    x_right_sin = []
    y_right_sin = []

    assert len(x)
    assert len(y)
    r, c = len(x), len(y)  # r行 c列


    for i in range(r):
        if i + 1 < len(x):
            c1_angle = math.atan(x[i + 1] - x[i])  # 时间序列c的每个点与前一个点的角度值
            c1_sin = math.sin(c1_angle)
            x_right_sin.append(c1_sin)

    x_right_sin.append(0)
    for j in range(c):
        if j + 1 < len(x):
            c1_angle = math.atan(y[j + 1] - y[j])  # 时间序列c的每个点与前一个点的角度值
            c1_sin = math.sin(c1_angle)
            y_right_sin.append(c1_sin)

    y_right_sin.append(0)
    return x_right_sin, y_right_sin


def xy_left_sin(x, y):
    x_left_sin = []
    y_left_sin = []

    assert len(x)
    assert len(y)
    r, c = len(x), len(y)  # r行 c列


    x_left_sin.append(0)
    for i in range(r):

        if i > 0:
            c1_angle = math.atan(x[i - 1] - x[i])  # 时间序列c的每个点与前一个点的角度值
            c1_sin = math.sin(c1_angle)
            x_left_sin.append(c1_sin)
    y_left_sin.append(0)
    for j in range(c):

        if j > 0:
            c1_angle = math.atan(y[j - 1] - y[j])  # 时间序列c的每个点与前一个点的角度值
            c1_sin = math.sin(c1_angle)
            y_left_sin.append(c1_sin)

    return x_left_sin, y_left_sin

def dist(x,y,weight,x_right_sin,y_right_sin,x_left_sin,y_left_sin):
    dist = weight * np.abs(x - y) + (1 - weight)/2 * (np.abs(np.array(x_right_sin)-np.array(y_right_sin))+np.abs(np.array(x_left_sin)-np.array(y_left_sin)))
    return dist



def __readFileTxt(filename):
    """读取txt文件"""

    f = open(filename)
    data = f.read()
    f.close()
    lineList = re.split('[ \n |:]', data)
    data = []
    label = []
    i = 0

    for line in lineList:
        if i % 2 == 0:
            data.append(line)
            i = i + 1
        else:
            label.append(line)
            i = i + 1
    return data, label

def ZscoreNormalization(x):
  """Z-score normaliaztion"""
  x = (x - np.mean(x)) / np.std(x)
  return x