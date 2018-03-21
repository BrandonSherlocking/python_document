class Person(object):
    """人的类"""
    def __init__(self, name):
        super(Person, self).__init__()
        self.name = name
        self.gun = None # 用来保存枪对象的引用
        self.hp = 100 # 用来保存人物血量

    def load_bullet(self, dan_jia_temp, bullet_temp):
        """把子弹装到弹夹中"""

        # 弹夹.保存子弹（子弹）
        dan_jia_temp.save_zidan(bullet_temp)

    def load_danjia(self, gun_temp, dan_jia_temp):

        """把弹夹安装到抢中"""

        #抢.保存弹夹（弹夹）
        gun_temp.save_danjia(dan_jia_temp)

    def naqiang(self, gun_temp):
        """拿起一把枪"""
        self.gun = gun_temp

    def __str__(self):
        if self.gun:
            return '%s的血量为：%d, 他有枪 %s' % (self.name, self.hp, self.gun)
        else:
            if self.hp > 0:
                return '%s的血量为：%d, 他没有枪' % (self.name, self.hp)
            else:
                return '%s 已挂' % self.name

    def kou_ban_ji(self, enemy):
        """让抢发射子弹去打敌人"""
        # 抢.开火（敌人）
        self.gun.fire(enemy)

    def blood(self, power):
        """根据杀伤力，掉相应的血量  """
        self.hp -= power


class Gun(object):
    """抢类"""
    def __init__(self, name):
        super(Gun, self).__init__()
        self.name = name # 用来记录抢的类型
        self.danjia = None # 用来记录弹夹对象的引用

    def save_danjia(self, dan_jia_temp):
        # 用一个属性来保存弹夹的引用
        self.danjia = dan_jia_temp

    def __str__(self):
        if self.danjia:
            return '抢的信息为：%s, %s' % (self.name, self.danjia)
        else:
            return '抢的信息为：%s, 这把抢中没有弹夹' % self.name

    def fire(self, enemy):
        """抢从弹夹中获取一发子弹，然后让子弹去击中敌人"""
        
        # 先从弹夹中取子弹
        # 弹夹.弹出一发子弹
        bullet_temp = self.danjia.tanchu_bullet()

        # 让这个子弹去伤害敌人
        if bullet_temp:
            # 子弹.打中敌人（敌人）
            bullet_temp.shot(enemy)
        else:
            print('弹夹中没有子弹了....')


class Danjia(object):
    """弹夹类"""
    def __init__(self, max_num):
        super(Danjia, self).__init__()
        self.max_num = max_num # 用来记录弹夹的最大容量
        self.bullet_list = [] # 用来记录所有的子弹的引用

    def save_zidan(self, bullet_temp):
        """将子弹保存"""
        self.bullet_list.append(bullet_temp)

    def __str__(self):
        return '弹夹的信息为：%d/%d' % (len(self.bullet_list), self.max_num)

    def tanchu_bullet(self):
        """弹出最上面的子弹"""
        if self.bullet_list:
            return self.bullet_list.pop()
        else:
            return None


class Bullet(object):
    """子弹"""
    def __init__(self, power):
        super(Bullet, self).__init__()
        self.power = power # 这颗子弹的威力    

    def shot(self, enemy):
        """让敌人掉血"""
        # 敌人.掉血（一颗子弹的威力）
        enemy.blood(self.power)


def main():
    """用来控制整个程序的流程"""

    # 1. 创建老王对象
    laowang = Person('老王')

    # 2. 创建一个抢对象
    ak47 = Gun('AK47')

    # 3. 创建一个弹夹对象
    dan_jia = Danjia(20)

    # 4. 创建一些子弹
    for i in range(15):
        zi_dan = Bullet(10)

    # 5. 老王把子弹安装到弹夹中
    # 老王.安装子弹到弹夹（弹夹，子弹）
        laowang.load_bullet(dan_jia, zi_dan)

    # 6. 老王把单间安装到抢中
    # 老王安装弹夹到抢中（抢，弹夹）
    laowang.load_danjia(ak47, dan_jia)

    # test:弹夹的信息
    # print(dan_jia)

    # text:测试抢的信息
    # print(ak47)

    # 7. 老王拿枪
    # 老王.拿枪（抢）
    laowang.naqiang(ak47)

    # test:测试老王对象
    print(laowang)

    # 8. 创建一个敌人
    gebi_laosong = Person('隔壁老宋')
    print(gebi_laosong)

    # 9. 老王开枪打敌人
    # 老王.扣扳机（隔壁老宋）
    for i in range(10):
        laowang.kou_ban_ji(gebi_laosong)
        print(gebi_laosong)
        print(laowang)


if __name__ == '__main__':
    main()