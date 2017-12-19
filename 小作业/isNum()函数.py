def multi(*b):
    a = 1
    for i in b:
        a *= i
    return a
b = multi (float(input('请输入要相乘的数字：'), float))
print(b)


