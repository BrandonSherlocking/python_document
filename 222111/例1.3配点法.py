'''
配点法求解，取两个未知数
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
# 替换x
r1 = r.subs(x, 1/3)
r2 = r.subs(x, 2/3)
# 解方程
ki = solve([r1, r2], [a1, a2])
print('a1:{:.4}  a2:{:.4}'.format(float(ki[a1]), float(ki[a2])))  # 转换为小数点型，保留4位小数
