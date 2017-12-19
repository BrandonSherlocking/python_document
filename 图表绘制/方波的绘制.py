#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-04-18 19:19:57
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import numpy as np
import matplotlib.pyplot as plt

# 产生一个方波(x,y),使用sin函数产生的，sinx>0,y=-1,sinx<0,y=1
x = np.linspace(-10, 10, 300)
y = []
for i in x:
    if np.sin(i) > 0:  # 调用sin，cos要使用np.sin，np.cos
        y.append(-1)
    else:
        y.append(1)
y = np.array(y)  # 需要把list转化成array，方便进行矩阵的运算


# 傅立叶函数，sin(nx),cos(nx),n是可以选择的
# 所以输入这个函数的三个参数分别为x，n，y
def fourier(x, y, n):
    x1 = []
    for i in range(n):
        x1.append(np.sin(x * i + x))
        x1.append(np.cos(x * i + x))
    m = np.mat(x1).T
    print(m.shape)
    y.shape = (y.shape[0], 1)
    p = m * np.linalg.inv(m.T * m) * m.T * y
    ym = np.array(p)
    ym.shape = (ym.shape[0],)
    return ym


plt.plot(x, y, color="g", label=u'方波')
plt.plot(x, fourier(x, y, 3), color='r', label='3')
plt.plot(x, fourier(x, y, 8), color='b', label='8')
plt.plot(x, fourier(x, y, 23), color='k', label='23')

plt.legend()
plt.axis('equal')
plt.show()