#英雄无敌
'''
Heroes beta-0.1
Sherlocking
2017-10-15
2017-10-28 map if 
'''
import random
#欢迎信息
welcome = 'wlelcome Heros world!'
mapmsg = '#######'
mapins = "\n-*- the world is like this -*-\n %s \n the'*'is you " % (mapmsg,)
instruction = '''
contrul your hero:
|'a' for left | 'd' for right | '''
print(welcome)

#初始化名字
name = input("input you name :")
hp = 100

if not name:
    name = 'player01'


def apple(hp):
    hp += 10
    return hp


def boom(hp):
    hp -= 10
    return hp


def ranD():
    s = [apple, boom]
    usermsg['hp'] = random.choice(s)(usermsg['hp'])
    print(usermsg['hp'])

usermsg = {'name': name, 'hp': hp}
print("you hero's name is :", usermsg['name'], 'Hp is :', usermsg['hp'])
print(mapins, instruction)

#用户操作
map1 = ['#', '#', '#', '#', '#', '#', '#']
point = 0
while 1:
    map1[point] = '*'
    print('you are here', ''.join(map1))
    userinput = input('go or quit:')
    if userinput == 'd' and point < 6:
        ranD()
        map1[point] = '#'
        point += 1
    elif userinput == 'a' and point > 0:
        map1[point] = '#'
        point -= 1
        ranD()
    elif userinput == 'quit':
        print('goodby!!')
        break
    else:
        print(instruction)








    
