# 雅克比解6.9

import numpy

def jcb(A,b,x0):
    # 迭代次数
    num = int(input('请输入迭代次数：'))
    # 求解精度
    ee = 1e-6
    # 获取矩阵列数
    D = numpy.linalg.inv(numpy.diag(numpy.diag(A)))

    # 判断
    if float(select) == 6.1:
        x = numpy.matrix([0.00, 0.00, 0.00, 0.00]).T
    elif float(select) == 6.5:
        x = numpy.matrix([0.00, 0.00, 0.00, 0.00, 0.00, 0.00]).T
    # 赋予初值
    x = x0

    # 迭代过程
    for k in range(num):
        r = b - A * x0
        x = x0 + D * r
        if numpy.linalg.norm(x-x0, numpy.inf) < ee:
            break
        x0 = x
    if k == num-1:
        print("求解精度过低，请设置更大的迭代次数")

    else:
        print("输入参数错误")

    return x, k+1

# 主函数
if __name__ == "__main__":
    # 题目选择
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
    elif float(select) == 6.5:
        Ra = int(6)
        A = numpy.matrix([[5, -3, 2, 0, 0, 0],
                          [-3, 8, -3, 2, 4, 0],
                          [2, -3, 8, -3, 0, 0],
                          [0, 2, -3, 7, -2, 1],
                          [0, 4, 0, -2, 7, -2],
                          [0, 0, 0, 1, -2, 4]], float).reshape(Ra, Ra)
        b = numpy.matrix([[6.],
                          [21.],
                          [0.],
                          [14.],
                          [22.],
                          [3.]])
        x0 = numpy.matrix([[0.],
                           [0.],
                           [0.],
                           [0.],
                           [0.],
                           [0.]])
    else:
        print('输入有误')
    #A = input("输入矩阵A：(使用numpy.matrix())")
    #Ra = int(input("请输入矩阵阶数："))
    #A = numpy.matrix(input("输入矩阵A（全部数据输入为一维即可）："),float).reshape(Ra,Ra)
    #b = numpy.matrix(input("输入矩阵b的转置矩阵："),float).T
    #x0 = numpy.matrix(input("输入矩阵x0的转置矩阵："),float).T
    # 求解
    x, k = jcb(A, b, x0)
    print("x为：{}，\n迭代次数：{}".format(x, k))
