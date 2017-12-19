__metaclass__ = type


class MyList:
    __mylist = []

    def __init__(self, *kwds, **args):
        self.__mylist = []
        for kwd in kwds:
            self.__mylist.append(kwd)

    def __add__(self, x):
        for i in range(0, len(self.__mylist)):
            self.__mylist[i] += x
        return self.__mylist

    def __sub__(self):
        pass

    def __mul__(self):
        pass

    def __div__(self):
        pass

    def __mod__(self):
        pass

    def __pow__(self):
        pass

    def __len__(self):
        pass  # len()
    
    def show(self):
        print(self.__mylist)

if __name__ == '__main__':
    l = MyList(1,2,23,4,5,6)
    l + 10
    l.show()

