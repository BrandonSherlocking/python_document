from numpy import *
import math

A = array([[5, -3, 1, 0],
           [-3, 11, -3, 1],
           [1, -3, 11, -3],
           [0, 1, -3, 6]])

b = array([[2],
           [14],
           [16],
           [17]])

x0 = array([[0],
            [0],
            [0],
            [0]])


er = 1 * (math.e) ** (-3) # 求解精度
D = linalg.inv(diag(diag(A)))
k = 1
for i in range(1, 101):  # 100次迭代
    r = b - A * x0
    x = x0 + D * r

select = input('请输入想要的解的题目（6.1或者6.5）：')
if float(select) == 6.1:
        Ra = int(4)
        A = numpy.matrix([[5., -3., 2., 0.],
                          [-3., 8., -3., 1.],
                          [2., -3., 8., -3.],
                          [0., 2., -3., 3.]]).reshape(Ra, Ra)
        b = numpy.matrix([[6.],
                          [5.],
                          [0.],
                          [8.]])
        x0 = numpy.matrix([[0.],
                           [0.],
                           [0.],
                           [0.]])