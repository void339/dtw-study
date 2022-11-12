# -*- coding: utf-8 -*-
"""
https://blog.csdn.net/chenxy_bwave/article/details/121052541
直接采用欧几里得距离作为相似性度量
"""

import numpy as np
import matplotlib.pyplot as plt


def euclid_dist(t1, t2):
    return np.sqrt(np.sum((t1 - t2) ** 2))


t = np.arange(100)
ts1 = 5 * np.sin(2 * np.pi * t * 0.05)  # 0.05Hz sin wave, 1Hz sampling rate, amplitude=5
ts2 = 3 * np.sin(2 * np.pi * t * 0.02)  # 0.02Hz sin wave, 1Hz sampling rate, amplitude=3
ts3 = 0.08 * t - 4

fig, axs = plt.subplots(figsize=(12, 8))
axs.plot(ts1)
axs.plot(ts2)
axs.plot(ts3)
axs.legend(['ts1: sin,0.05Hz, amplitude=5',
            'ts2: sin,0.02Hz, amplitude=3',
            'ts3: line with slope = 0.08'])

euclidean_dist_12 = euclid_dist(ts1, ts2)
euclidean_dist_13 = euclid_dist(ts1, ts3)
euclidean_dist_23 = euclid_dist(ts2, ts3)
print('euclidean_dist_12 = {0:6.2f}'.format(euclidean_dist_12))
print('euclidean_dist_13 = {0:6.2f}'.format(euclidean_dist_13))
print('euclidean_dist_23 = {0:6.2f}'.format(euclidean_dist_23))

def DTWDistance(s1, s2):
    DTW = {}

    for i in range(len(s1)):
        DTW[(i, -1)] = float('inf')
    for i in range(len(s2)):
        DTW[(-1, i)] = float('inf')
    DTW[(-1, -1)] = 0

    for i in range(len(s1)):
        for j in range(len(s2)):
            dist = (s1[i] - s2[j]) ** 2
            DTW[(i, j)] = dist + min(DTW[(i - 1, j)], DTW[(i, j - 1)], DTW[(i - 1, j - 1)])

    return np.sqrt(DTW[len(s1) - 1, len(s2) - 1])


dtw_dist_12 = DTWDistance(ts1, ts2)
dtw_dist_13 = DTWDistance(ts1, ts3)

dtw_dist_23 = DTWDistance(ts2, ts3)

print('dtw_dist_12 = {0:6.2f}'.format(dtw_dist_12))
print('dtw_dist_23 = {0:6.2f}'.format(dtw_dist_23))
print('dtw_dist_13 = {0:6.2f}'.format(dtw_dist_13))

plt.show()
