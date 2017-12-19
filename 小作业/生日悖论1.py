def fact(n):
    if n == 1:
        return n
    else:
        return n*fact(n-1)

def birB(k):
    p1 = fact(365)/((365**k)*(fact(365 - k)))
    return 1 - p1
vaul = int(input('请输入房间里的人：'))
anw = birB(vaul)
print('房间里{}人至少有两个人的生日相同的概率是：'.format(anw))