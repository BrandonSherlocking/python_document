#命名空间，，类的命名空间 self：对象本身

class Human:
    '''
                      This is Human class obstring
    '''

    name = 'ren'
    age = '25'
    gender = 'male'
    _money = 8000

    def __init__(self, name, age):# 构造函数，生成对象时自动调用》》》
        print('#'*50)
        self.name = name
        self.age = age
        print('#'*50)
        
        
    def __str__(self):
        msg = 'hi! i am the object of Human!!'
        return msg

    
    def say(self):
        print('my name is %s i have %d' % (self.name, self._money))
        self.__lie()
        
        

    def __lie(self):
        print('i have 5000')




# zhangshan._Human__lie() # 访问私有特性

print('-'*20)
zhangshan = Human('zhangshan', 30) #类被实例化成对象时，就开始执行__init__()（打印
# ‘#’和进行传值）
print(zhangshan.name, zhangshan.age)


