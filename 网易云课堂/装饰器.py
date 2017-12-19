# 装饰器，传递函数，把函数传递给另外一个函数，在赋值给另外一个函数
# 语法糖，@ 精简装饰器的代码
import time
def deco(func):
    def wrapper():
        startT = time.time()
        func()
        endT = time.time()
        msecs = (endT - startT)*1000
        print("it's %f ms" % msecs)
    return wrapper

@deco
def myfunc():
              print('myfunc start……')
              time.sleep(1.7)
              print('myfunc end……')


print('myfunc is',myfunc.__name__)
# myfunc = deco(myfunc)
print('#'*50)
print('myfunc is',myfunc.__name__)
myfunc()
