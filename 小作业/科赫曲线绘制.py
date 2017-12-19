import turtle
def koch(size, n):
    if n == 0:
        turtle.fd(size)
    else:
        for angle in [0, 60, -120, 60]:
            turtle.left(angle)
            koch(size/3, n-1)

def main():
    turtle.setup(1900,900)
    turtle.speed(100000)
    turtle.penup()
    turtle.goto(-400, 100)
    turtle.pendown()
    turtle.pensize(2)
    level = 5
    size = 600
    koch(size, level)
    turtle.right(120)
    koch(size, level)
    turtle.right(120)
    koch(size, level)
    turtle.hideturtle()
main()
