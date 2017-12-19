'''
import time
for i in range(101):
    print('{\r:3}%'.format(i),end='')
    time.sleep(0.05)
'''
#结合单行和精度条
import time
scale = 50
print('执行开始'.center(scale,'-'))
t=time.clock()
for i in range(scale+1):
    a='*'*i
    b='.'*(scale-i)
    c=(i/scale*100)
    t-=time.clock()
    print('\r{:^3.0f}%[{}->{}]{:.2f}s'.format(c,a,b,-t),end='')
    time.sleep(0.05)
print('\n'+'执行结束'.center(scale,'-'))
