'''
里兹法求解，两个未知数
'''

#导入库
from sympy import*
# 声明变量
x = Symbol('x')
a1 = Symbol('a1')
# 选取一项近似解
u = a1*(sin(x) - x*sin(1))
# 求一次积分
r = diff(u, x)
# 简化表达式
f = (-1/2)*r**2 + (1/2)*u**2+u*x
# 求定积分
g = integrate(f, (x, 0, 1))
k = diff(g, a1)
# 求解
ki = solve([k], [a1])
# 转换为小数点型，保留4位小数，打印结果
a2 = -float(ki[a1]*sin(1))
print('a1:{:.4} ---- a2:{:.4}'.format(ki[a1], a2))
