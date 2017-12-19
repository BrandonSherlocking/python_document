def two_level(n):
    ls = str(abs(eval(n)))
    leng = len(ls)
    num = ls.count('2')
    if int(n) < 0:
        if int(n) % 2 == 0:
            num *= 2
        num *= 1.5
        leve = num/leng
        result1 = '{:.2f}%'.format(leve*100)
        return result1
    else:
        if int(n) % 2 == 0:
            num *= 2
        leve = num / leng
        result2 = '{:.2f}%'.format(leve*100)
        return result2


in_put = input('please input number to judge your two_level:')
result = two_level(in_put)
print('you two_level is:', result)
