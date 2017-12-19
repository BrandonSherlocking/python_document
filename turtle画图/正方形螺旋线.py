#正方形螺旋线python代码
from turtle import *
goto(0,0)
pencolor('red')
for i in range(1,90):
    fd(5+3*i)
    left(90)
