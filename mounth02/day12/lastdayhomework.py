# 玩家类
class Play:
    def __init__(self, hp, atk):
        self.hp=hp
        self.atk=atk
    def attack(self,enemy):
        print('打')
        enemy.damage(self.atk)

    def damage(self, value):
        print('被打')
        self.hp -= value
        if self.hp <= 0:
            print('game over')
class Enemy:
    def __init__(self, hp, atk):
        self.hp = hp
        self.atk = atk
    def attack(self,enemy):
        print('打')
        enemy.damage(self.atk)

    def damage(self,value):
        print('被打')
        self.hp-=value
        if self.hp<=0:
            print('动画')

gbl=Enemy(10,10)
a=Play(10,20)
a.attack(gbl)