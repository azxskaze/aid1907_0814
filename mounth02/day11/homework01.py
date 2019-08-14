class Player:
    def __init__(self,name,atk,hp):
        self.name=name
        self.atk=atk
        self.hp=hp
    def attack(self,obj):
        obj.hp-=self.atk
        if obj.hp<=0:
            obj.die()
    def die(self):
        print('you die')
        print('game over')

class Enemy:
    def __init__(self,name,atk,hp):
        self.name=name
        self.atk = atk
        self.hp = hp
    def attack(self, obj):
        obj.hp -= self.atk
        if obj.hp<=0:
            obj.die()

    def die(self):
        print('死亡动画')
        print(self.name,'被消灭')
ming=Player('小明',20,60)
enemy_list=[Enemy('地狱犬1',10,30),
            Enemy('地狱犬2',10,30)]
# monster=Enemy('地狱犬1',10,30)
# monster2=Enemy('地狱犬2',10,30)
def pd(obj):
    if obj.hp <= 0:
        return 1

while len(enemy_list):
    if pd(ming):
        break
    for i in enemy_list[::-1]:
        if i.hp <= 0:
            enemy_list.remove(i)
    if len(enemy_list)==0:
        print('you win')
        break
    ming.attack(enemy_list[0])

    print('*',ming.hp,len(enemy_list))
    for i in enemy_list:
        print('**',i.hp)

    if len(enemy_list)==0:
        print('you win')
        break

    for i in enemy_list[::-1]:
        if i.hp<=0:
            enemy_list.remove(i)
        if ming.hp <= 0:
            print('die die die')
            break
        i.attack(ming)






# ming.attack(monster)
# monster.attack(ming)
# monster2.attack(ming)
#
# ming.attack(monster2)
# ming.attack(monster)





