
#https://blog.csdn.net/weixin_43945848/article/details/120777669
import numpy as np
#来自官方库的示例，代码未动，但注解原创。
#y是x的子序列，从x的第三个数字开始一一匹配
x = np.array([2, 5, 4]).reshape(-1, 1)
y = np.array([1, 2, 3]).reshape(-1, 1)
#https://blog.csdn.net/weixin_39729115/article/details/109926607
# python引入自己写的文件_python引入导入自定义模块和外部文件
from dtw01 import *
#曼哈顿距离定义，各点相减的绝对值


#计算出总距离，耗费矩阵，累计耗费矩阵，在矩阵上的路径
# d, cost_matrix, acc_cost_matrix, path = dtw(x, y, dist=manhattan_distance)
#
# a,b = path
#
# print(a,'a')
# print(b,'b')
#
# r, c = len(x), len(y)
# D0 = zeros((r, c))
#
# c = [element for lis in [a,b] for element in lis]
#
#
# for i in range(len(c)-len(a)):
#
#     D0[c[i],c[i+len(a)]] = 1
#
# print(D0,'计数矩阵')
#
# sum_Row = []
# sum_List = []
#
# for i in D0:
#     a = sum(i)
#     sum_Row.append(a)
#
# for i in range(D0.shape[1]):
#     a = sum(D0[:,i])
#     sum_List.append(a)
#
# print(sum_Row,sum_List ,'行列和')


dist = lambda x, y: np.abs(x - y)

warp = 1
w = inf
s = 1.0

assert len(x)
assert len(y)
assert isinf(w) or (w >= abs(len(x) - len(y)))
assert s > 0

r, c = len(x), len(y) # r行 c列

D0 = zeros((r + 1, c + 1))
D0[0, 1:] = inf
D0[1:, 0] = inf
print(D0, 'D0-1 初始化累计距离矩阵')

Dq = zeros((r + 1, c + 1))
Dq[0, 1:] = 1
Dq[1:, 0] = 1
Dq[0, 0] = 1
print(Dq, 'Dq-1 初始化累计距离矩阵')

Dc = zeros((r + 1, c + 1))
Dc[0, 1:] = 1
Dc[1:, 0] = 1
Dc[0, 0] = 1
print(Dc, 'Dc-1 初始化累计距离矩阵')

D1 = D0[1:, 1:]  # view
print(D1, 'D1-1')
for i in range(r):
    for j in range(c):
        if (isinf(w) or (max(0, i - w) <= j <= min(c, i + w))):
            D1[i, j] = dist(x[i], y[j])
print(D1, 'D1-2 计算距离矩阵')
C = D1.copy()
print(C, 'C')
jrange = range(c)
print(jrange, 'jrange-0 列数')
print(D0, 'D0-2 赋值距离后但还未累计的累计距离矩阵')
for i in range(r):  # i 行数
    for j in jrange:  # j 列数
        min_list = [D0[i, j]]
        # print(min_list, 'min_list-j')
        for k in range(1, warp + 1):
            if 0<r/c<=1/2 or 0<c/r<1/2:
                i_k = min(i + k, r)
                j_k = min(j + k, c)
                min_list += [D0[i_k, j] + Dc[i + 1, j]*(r+c)/(2*max(r, c)*D1[i, j]), D0[i, j_k] + Dq[i,j+1]*(r+c)/(2*max(r, c))*D1[i, j]]
                print(r,c,D0[i_k, j],D1[i, j],'r,c,D0[i_k, j],D1[i, j]')
            else:
                i_k = min(i + k, r)
                j_k = min(j + k, c)
                min_list += [D0[i_k, j] + Dc[i + 1, j]*(2*max(r, c)/(r+c)*D1[i, j]), D0[i, j_k] + Dq[i,j+1]*2*max(r, c)/(r+c)*D1[i, j]]
                print(r, c,  D0[i, j_k], D1[i, j],D0[i, j_k] + Dq[i,j+1]*2*max(r, c)/(r+c)*D1[i, j],D1[i, j], 'r,c,D0[i_k, j],D1[i, j],add')
            print(min_list, 'min_list-k')
        D1[i, j] += min(min_list)
        print(D1[i, j])
        print(min_list.index(min(min_list)))
        if min_list.index(min(min_list)) == 0:
            Dq[i+1, j+1] = 1
            Dc[i + 1, j + 1] = 1
        if min_list.index(min(min_list)) == 1:
            Dq[i + 1, j + 1] = Dq[i + 1, j] + 1
            Dc[i + 1, j + 1] = 1
        if min_list.index(min(min_list)) == 2:
            Dq[i+1, j+1] = 1
            Dc[i + 1, j + 1] = Dc[i, j + 1] + 1
print(D1, 'D1-3 累计距离矩阵')
print(Dq, 'Dq-3 累计距离矩阵')
print(Dc, 'Dc-3 累计距离矩阵')
def _traceback(D):
    i, j = array(D.shape) - 2
    p, q = [i], [j]
    print(D)
    print(i, j, 'i, j')
    print(p, q, 'p, q')
    while (i > 0) or (j > 0):
        tb = argmin((D[i, j], D[i, j + 1], D[i + 1, j]))
        if tb == 0:
            i -= 1
            j -= 1
        elif tb == 1:
            i -= 1
        else:  # (tb == 2):
            j -= 1
        p.insert(0, i)
        q.insert(0, j)
    print(array(p), 'array(p)')
    print(array(q), 'array(q)')
    return array(p), array(q)

path = _traceback(D0)

print(path)