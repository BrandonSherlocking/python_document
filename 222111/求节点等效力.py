'''
求节点等效力
'''

#导入库
from sympy import*
# 声明变量
b = Symbol('b')
a = 1
# 节点坐标
x1, y1 = 40, 50
x8, y8 = 35, 35
x4, y4 = 30, 20
'''
1,8,4节点的插值函数。根据插值函数的构成原理,
节点2,3,5,6,7的插值函数必包含(1-a),而此处a=1,
所以不用列出其他节点的插值函数
'''
N1 = (1+a)*(1+b)*(a+b-1)/4
N8 = (1+a)*(1-b**2)/2
N4 = (1+a)*(1-b)*(a-b-1)/4
# 计算弧长
x = x1*N1 + x8*N8 + x4*N4
y = y1*N1 + y8*N8 + y4*N4
dx_b = diff(x, b)
dy_b = diff(y, b)
s = (dx_b**2+dy_b**2)**0.5
# 等效力计算的被积函数:节点的插值函数*应力分量*弧长
p = 1              #均布载荷大小
f1x = N1*p*s
f8x = N8*p*s
f4x = N4*p*s
# 替换b
P1x = f1x.subs(b, -1/sqrt(3)) + f1x.subs(b, 1/sqrt(3))
P8x = f8x.subs(b, -1/sqrt(3)) + f8x.subs(b, 1/sqrt(3))
P4x = f4x.subs(b, -1/sqrt(3)) + f4x.subs(b, 1/sqrt(3))

# 解方程
print('P1x:{:.4}  P8x:{:.4}  P4x:{:.4}'.format(float(P1x),\
float(P8x), float(P4x)))   # 转换为小数点型，保留4位小数
