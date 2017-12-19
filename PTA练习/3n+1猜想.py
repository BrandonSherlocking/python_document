def guess(number):
    i = 0
    if number < 1:
        print('enter error')
    while number != 1:
        if number % 2 == 0:
            number /= 2
        else:
            number = (number*3 + 1) / 2
        i += 1
    return i


result = guess(eval(input('please enter iterable number:')))
print(result)
