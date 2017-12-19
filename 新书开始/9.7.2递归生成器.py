def flatten(nested):
    try:
        try:
            nested + ''
        except TypeError:
            print('1')
            pass
        else:
            print('2')
            raise TypeError

        for sublist in nested:
            print('ss')
            for element in flatten(sublist):
                yield element
    except TypeError:
        print('3')
        yield nested


#print(list(flatten(['foo', ['bar', ['baz']]])))
list1 = flatten([1, [2, [3, [4]]]])
print(list(list1))
