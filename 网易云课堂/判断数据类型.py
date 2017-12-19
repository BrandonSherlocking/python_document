#打印出输入的数据类型


a=input ('please input shome word:')
try:
    b=int(a)
    c=complex(a)
    d=str(a)
    if isinstance (b,int)==True:
        print('wow, you input type is:'+'int')    
except:
    print('wow, how fuck are you input')
else:
    if isinstance (c,complex)==True:
        print('wow, you input type is:'+'complex')
    elif isinstance (d,str)==True:
        print ('wow,you input type is :'+'str')
   
