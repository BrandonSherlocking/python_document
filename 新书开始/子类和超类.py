class Filter:
    def init(self):
        self.bolocked = []
    def filter(self, sequence):
        return [x for x in sequence if x not in self.blocked]


class SPAMFilter(Filter):
    def init(self):
        self.blocked = ['SPAM']

# s = SPAMFilter()
# s.init()
# s.filter(['SPAM','SPAM','SPAM','SPAM','SPAM','eggs','bacon', 'SPAM'])



'''
多个超类，子类：TalkingCalculator

'''
class Calculator:
    def calculate(self, expression):
        self.value = eval(expression)


class Talker:
    def talk(self):
        print('Hi, my value is', self.value)


class TalkingCalculator(Calculator, Talker):
    pass


