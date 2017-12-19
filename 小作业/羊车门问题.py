from random import *
Time = 1000000
MyFirstChoice = 0
MyChangeChoice = 0
for i in range(Time):
    box = [1, 2, 3]
    carInDoor = box[-1]
    MyGuess = choice(box)
    if carInDoor == MyGuess:
        MyFirstChoice += 1
    else:
        MyChangeChoice += 1
print('不变选择选中车的概率是{:.6}'.format(MyFirstChoice/Time))
print('改变选择选中车的概率是{:.6}'.format(MyChangeChoice/Time))