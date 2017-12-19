#待解决问题，如何让用户输入参数，自定义

Setup=input('do you want to draw a snke? \npleae input some redius,angle,length :')
import turtle
def drawSnake(radius,angle,length):
    turtle.seth(-45)
    for i in range(length):
        turtle.circle(redius,angle)
        turtle.circle(-redius,angle)
    turtle.circle(redius,angle/2)
    turtle.fd(40)
    turtle.circle(16,180)
    turtle.fd(40*3/2)
turtle.setup(1000,400,500,200)
turtle.penup()
turtle.fd(-250)
turtle.pendown()
turtle.pensize(25)
turtle.pencolor('red')
drawSnake(eval(Setup[0]),eval(Setup[1]),eval(Setup[2]))
turtle.done()
