__metaclass__ = type


class Bird:
    def __init__(self):
        self.hungry = True

    def eat(self):
        if self.hungry:
            print('Aaaah……')
            self.hungry = False
        else:
            print('No Thanks!')


class SongBird(Bird):
    def __init__(self):
        super(SongBird, self).__init__()
        self.sound = 'Squawk!'

    def sing(self):
        print(self.sound)


sb = SongBird()
print('Bird is sing:', end=' ')
sb.sing()
print('Bird is eat:', end=' ')
sb.eat()
print('Bird is eat:', end=' ')
sb.eat()
