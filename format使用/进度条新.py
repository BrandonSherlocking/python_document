import time
scale = 5
for i in range(scale+1):
    a = '.'*i
    print('\rStarting! {}'.format(a), end='')
    time.sleep(0.5)
print('{:<}'.format(' Done!!'))
