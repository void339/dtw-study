#https://blog.csdn.net/weixin_43945848/article/details/120777669
import numpy as np
#来自官方库的示例，代码未动，但注解原创。
#y是x的子序列，从x的第三个数字开始一一匹配
x = np.array([2, 0, 1, 1]).reshape(-1, 1)
y = np.array([1, 1, 2]).reshape(-1, 1)
#https://blog.csdn.net/weixin_39729115/article/details/109926607
# python引入自己写的文件_python引入导入自定义模块和外部文件
from dtw01 import *
#曼哈顿距离定义，各点相减的绝对值
manhattan_distance = lambda x, y: np.abs(x - y)

#计算出总距离，耗费矩阵，累计耗费矩阵，在矩阵上的路径
d, cost_matrix, acc_cost_matrix, path = dtw(x, y, dist=manhattan_distance)

print(d)
#计算得出2.0

import matplotlib.pyplot as plt

plt.imshow(acc_cost_matrix.T, origin='lower', cmap='gray', interpolation='nearest')
#lower参数表示上下颠倒，注意这里矩阵行列转置
plt.plot(path[0], path[1], 'w')
#path包含两个array

#plt.plot(x)
#plt.plot(y)
#显示xy轴

plt.show()

import dtw
