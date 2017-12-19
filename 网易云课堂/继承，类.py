class Father:
    money = 10000000
    __money = 1000000000000

    def drive(self):
        print('i can drive a car!!')

class Father1:
    money1 = 1000000000


class Son(Father):

    def drive(self):
        print('i can drive tank!')
        return super().drive() # 超类，super函数， 特殊的构造方法
        
    def pay(self):
        return super().money

    x = property(drive, pay)


jerry = Son()
print(jerry.money)
print(jerry.drive())
print(jerry._Father__money) # python没有绝对的私有
print('='*20)
#jerry.x
print(jerry.pay())

    
