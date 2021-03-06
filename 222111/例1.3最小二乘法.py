'''
最小二乘法求解，取两个未知数
'''

#导入库
from sympy import*
# 声明变量
x = Symbol('x')
a1 = Symbol('a1')
a2 = Symbol('a2')
# 选取一项近似解
u = x*(1-x)*(a1 + a2*x)
# 求二次积分
r = diff(u, x, 2)
# 余量
r += u+x
# 最小二乘法的权
w1 = diff(r, a1)
w2 = diff(r, a2)
# 简化表达式
f1 = r*w1
f2 = r*w2
# 求定积分
g1 = integrate(f1, (x, 0, 1))
g2 = integrate(f2, (x, 0, 1))
# 打印结果
ki = solve([g1, g2], [a1, a2])
print('a1:{:.4}  a2:{:.4}'.format(float(ki[a1]), float(ki[a2])))  # 转换为小数点型，保留4位小数
