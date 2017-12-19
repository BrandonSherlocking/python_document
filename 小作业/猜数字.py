from random import *
N = 0
R = randint(1, 100)
while True:
    try:
        RN = eval(input('请你输入想要猜的文字的范围(用数字表示)：'))
    except :
        print('输入错误，请输入数字范围')
    else:
        while True:
            seed(R)
            N += 1
            rand = randint(0, RN)
            try:
                num = eval(input('请猜猜我想要的{}以内的数字：'.format(RN)))
            except :
                print('你输入的不是数字哦，请输入数字')
            else:
                if num == rand:
                    print('你猜了{}次，猜中了'.format(N))
                    break
                if num < rand:
                    print('你猜的有点小哦')
                if num > rand:
                    print('你猜的有点大哦')


