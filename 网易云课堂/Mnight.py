#打印出9*9口诀

'''

for i in range(1,10):
    for j in range(1,i+1):
        result=j*i
        print('%d*%d=%-3d'%(j,i,result),end='')
    print()

'''


def nightM():
    for i in range(1, 10):
        for j in range(1, i + 1):
            print('{}*{}={:2}  '.format(j, i, i * j), end='')
        print()


