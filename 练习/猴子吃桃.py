'''
猴子第一天摘下若干个桃子，当即吃了一半，还不过瘾，有多吃了一个；
第二天早上又将剩下的桃子吃掉一半，又多吃一个。以后每天早上都吃了前一天剩下的一半多一个。
到第五天早上想吃时，见只剩一个桃子了。
猴子第一天摘了多少个桃子
'''

n = 1
for i in range(5, 0, -1):
    n = (n+1) << 1
print(n)
