'''
超松弛迭代法
求解练习题6.5
'''
from numpy import *  # 导入numpy库

# 矩阵
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


n = 6   # 矩阵列数
er = 1 * (math.e) ** (-6)  # 求解精度
omga = 1.2   # 超松弛因子
x = x0.copy()
D = zeros((4, 4))
D1 = zeros((4, 4))
for k in range(1, 101):  # 100次迭代
    for i in range(n):
        for j in range(1, n+1):
            D[i, j-1] += sum(A[i, j-1])    # A的第i行，第1列到j-1列求和
        for l in range(j+1, n+1):
            D[i, l] += sum(A[i, l])        # A的第i行，第j+1列到n列求和
        x[i].append = x0[i] + omga * (b[i] - D[i, j-1]*x[0:i - 1] - D[i, l]*x0[i:n]) / A[i, i]
    while linalg.norm(x - x0, ord=inf) < er:
        break
    x0 = x

print('最终所求矩阵：'x)
print('迭代次数：'k)
