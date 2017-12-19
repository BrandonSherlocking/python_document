exchange=input('请输入美元或者人民币: ')
if exchange[-1] in ['r','R']:
    D=eval(exchange[0:-1])/6.653
    print('转换后是：{:.6f}美元'.format(D))
elif exchange[-1] in ['m','D','M']:
    R=eval(exchange[0:-1])*6.6530
    print('转换后是：{:.6f}人民币'.format(R))
else:
    print('你输入的是啥，不对啊')
