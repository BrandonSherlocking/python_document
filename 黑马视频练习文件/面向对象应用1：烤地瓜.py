class SweetPotato:

    def __init__(self):
        self.cookedString = '生的'
        self.cookedLevel = 0
        self.condiment = []

    def __str__(self):
        return '地瓜 状态:%s(%d) 添加的佐料是：%s' % (self.cookedString, self.cookedLevel, str(self.condiment))

    def cook(self, cooked_time):

        self.cookedLevel += cooked_time

        if (self.cookedLevel >= 0) and (self.cookedLevel < 3):
            self.cookedString = '生的'
        elif (self.cookedLevel >= 3) and (self.cookedLevel < 5):
            self.cookedString = '半生不熟'
        elif (self.cookedLevel >= 5) and (self.cookedLevel < 8):
            self.cookedString = '熟了'
        elif self.cookedLevel > 8:
            self.cookedString = '烤糊了'

    def add_condiments(self, item):
        self.condiment.append(item)


# 创建一个地瓜对象
di_gua = SweetPotato()
print(di_gua)

# 开始烤地瓜
di_gua.cook(1)
print(di_gua)
di_gua.cook(1)
print(di_gua)
di_gua.cook(1)
di_gua.add_condiments('芥末')
print(di_gua)
di_gua.cook(1)
di_gua.add_condiments('番茄')
print(di_gua)
di_gua.cook(1)
di_gua.add_condiments('孜然')
print(di_gua)
di_gua.cook(1)
di_gua.add_condiments('辣椒酱')
print(di_gua)
