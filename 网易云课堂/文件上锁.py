'''
heroes beta-0.2-1
'''

import os
welcome = 'welcome to Herores world!'
i = 0
while True:
    if os.path.isfile('lock.log'):
        print('locked')
        break
    username = input('login:')
    password = input('password')
    if username == 'sher' and password == '123':
        pass
    else:
        i += 1
        if i == 3:
            open('lock.log', 'w').write(username)
            print('locked by %s' % username)
            break
        continue
    print(welcome)

