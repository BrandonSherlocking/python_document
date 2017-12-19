while 1:
    n = input('please input some number :')
    if n == 'q' or n == 'quit':
        break
    Sum = []
    for i in range(1, int(n) + 1):
        Sum.append(i)
    print('you sum result is:', sum(Sum))


'''

n=input('please input some number :')
Sum=0
for i in range(1,int(n)+1):
    Sum+=i
print('you sum result is:',Sum)


'''


