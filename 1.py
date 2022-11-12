import numpy as np
from dtw01 import *
#y是x的子序列，从x的第三个数字开始一一匹配
x = np.array([2, 5, 6]).reshape(-1, 1)
y = np.array([6, 4, 6]).reshape(-1, 1)
assert len(x)
assert len(y)
r, c = len(x), len(y) # r行 c列
import math
'''
for i in range(0,r):
    for j in range(0,c):
        print(i,j,"i j")
        if 0<i<r and 0<j<c:
            r1_angle = math.atan(x[i+1] - x[i])
            c1_angle = math.atan(y[j+1] - y[j])
            r0_angle = math.atan(x[i] - x[i-1])
            c0_angle = math.atan(y[j] - y[j-1])
            print(r1_angle, c1_angle,r0_angle, c0_angle, "angle")
            a = math.sin(r1_angle)
            b = math.sin(c1_angle)
            d = math.sin(r0_angle)
            e = math.sin(r0_angle)
            print(a, b, c, d, "a b c d")
        if i==0 and j==0:
            print("zzz")
'''
for i in range(r):
    if 0 < i < r:
        r1_angle = math.atan(x[i] - x[i-1])#时间序列r的每个点与前一个点的角度值
        print(x[i] - x[i-1], "x[i] - x[i-1]")
        print(i-1, i, r1_angle, "i-1,i,r1_angle")
        r1_sin = math.sin(r1_angle)
        print(r1_sin, "r1_sin")

for j in range(c):
    if 0 < j < c:
        c1_angle = math.atan(y[j] - y[j-1])#时间序列c的每个点与前一个点的角度值
        print(y[j] - y[j-1], "y[j] - y[j-1]")
        print(j-1, j, c1_angle, "j-1, j, c1_angle")
        c1_sin = math.sin(c1_angle)
        print(c1_sin, "c1_sin")

'''
i, j = array(D.shape) - 2
p, q = [i], [j]
p.insert(0, i)
q.insert(0, j)
print(array(p), 'array(p)')
print(array(q), 'array(q)')
'''