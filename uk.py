import random


def inf_print(sentence=''):
    left = '<'
    right = '>'
    print(left*10, '{:^10}'.format(sentence), right*10)
    sente = 'The game rule is : \n' \
            'three times bet, each time the number is 1 to 6\n' \
            'the small is 3 to 9, the big is 10 to 18\n' \
            'if you win, you will gain same money for you capital,\n' \
            'if you lose, you will lose total money'
    print('*'*50)
    print(sente)
    print('*'*50)


def roll_dice(number=3):
    inf_print(sentence='ROLE THE DICE!')
    points = []
    while number > 0:
        point = random.randrange(1, 7)
        points.append(point)
        number -= 1
    return points


def roll_result(total):
    if 11 <= total <= 18:
        return 'Big', 'b', 'big'
    if 3 <= total <= 10:
        return 'Small', 's', 'small'


def you_win(you_choice, you_capital):
    points = roll_dice(number=3)
    total = sum(points)
    win = you_choice in roll_result(total)
    if win:
        print('The point are', points, 'You win!')
        print('You gained {}, you have {} now'.format(you_capital, you_capital * 2))
    else:
        print('The point are', points, 'You lose!')
        print('You lost {}, you have {} now'.format(you_capital, 0))


def start_game():
    print('<'*10, 'GAME STARTS!!', '>'*10)
    you_choice = input('Big or Small:')
    choices = ['Big', 'Small', 'big', 'small', 'b', 's']
    if you_choice in choices:
        you_capital = eval(input('How much you wanna bat? ——>'))
        you_win(you_choice, you_capital)
    else:
        print('Invalid Words')
        start_game()


start_game()
