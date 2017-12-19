class PrivateClass:
    ''' 这是私有属性，现在对他进行返回值和修改'''
    __pr_money = 20000
    def reprm(self):
        return self.__pr_money

    def fixprm(self, value):
        self.__pr_money = int(value)
        return self.__pr_money    
