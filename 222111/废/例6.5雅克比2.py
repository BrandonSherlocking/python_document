'''
雅克比跌打法
求解练习题6.5
'''
from numpy import *
import math

A = array([[5, -3, 2, 0, 0, 0],
           [-3, 8, -3, 2, 4, 0],
           [2, -3, 8, -3, 0, 0],
           [0, 2, -3, 7, -2, 1],
           [0, 4, 0, -2, 7, -2],
           [0, 0, 0, 1, -2, 4]])

b = array([[6],
           [21],
           [0],
           [14],
           [22],
           [3]])

x0 = array([[0],
            [0],
            [0],
            [0],
            [0],
            [0]])


er = 1 * (math.e) ** (-3) # 求解精度
D = linalg.inv(diag(diag(A)))
k = 1
for i in range(1, 101):  # 100次迭代
    r = b - A * x0
    x = x0 + D * r
    if linalg.norm(x - x0, inf) < er:
        k += 1
        break
    else:
        x0 = x

print(x0)
print(k)