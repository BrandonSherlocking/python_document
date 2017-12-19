from random import *


def main():
    description()
    print()
    ppA, ppB, n = getInput()
    winsA, winsB = nGame(ppA, ppB, n)
    print()
    printSummary(winsA, winsB)


def description():
    print('{:*<43}'.format(''))
    print('{:<13}{:^}{:>12}'.format('*', '这里是乒乓球大赛现场', '*'))
    print('{:<6}A和B的能力值(以0到1之间的小数表示){:>6}'.format('*', '*'))
    print('{:<13}每场比赛进行11回合{:>14}'.format('*', '*'))
    print('{:*<43}'.format(''))


def getInput():
    a = eval(input('>>请输入选手A的能力值（0到1之间）:'))
    b = eval(input('>>请输入选手B的能力值（0到1之间）:'))
    n = eval(input('>>请输入比赛次数:'))
    return a, b, n


def gameOver(a, b):
    return a == 11 or b == 11


def oneGame(ppA, ppB):
    scoreA, scoreB = 0, 0
    seaveing = ['A', 'B']
    rseve = choice(seaveing)
    while not gameOver(scoreA, scoreB):
        if rseve == 'A':
            if random() < ppA:
                scoreA += 1
            else:
                scoreB += 1
            rseve = 'B'
        else:
            if random() < ppB:
                scoreB += 1
            else:
                scoreA += 1
            rseve = 'A'
    return scoreA, scoreB


def nGame(ppA, ppB, n):
    winsA, winsB = 0, 0
    for i in range(n):
        soreA, soreB = oneGame(ppA, ppB)
        if soreA > soreB:
            winsA += 1
        else:
            winsB += 1
    return winsA, winsB


def printSummary(winsA, winsB):
    n = winsA + winsB
    print('竞技分析开始，共模拟{}场比赛'.format(n).center(32, '='))
    print()
    print('选手A获胜{}场比赛，占比{:0.1%}'.format(winsA, winsA/n).center(30))
    print('选手B获胜{}场比赛，占比{:0.1%}'.format(winsB, winsB/n).center(30))


main()

