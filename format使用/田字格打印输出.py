for i in range(10):
    sa = ''
    for j in range(10):
        if i in [0, 4, 9]:
            st = '-'
            if j in [0, 4, 9]:
                st = '+'
            sa +='{}'.format(st)
        else:
            if j in [0,4,9]:
                sa += '|'
            else:
                sa += ' '
    print(sa)
for i in range(10):
    str = ''
    for j in range(10):
        if i in [0, 4, 9]:
            st = '-'
            if j in [0, 4, 9]:
                st = '+'
            str += '{}'.format(st)
        else:
            if j in [0, 4, 9]:
                str += '|'
            else:
                str += ' '

    print(str)