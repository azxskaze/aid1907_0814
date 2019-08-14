class Enemy:

    def __init__(self, name, hp, ap, mt):
        self.name = name
        self.set_hp(hp)

        self.set_ap(ap)
        self.mt = mt
    def show_enemy(self):
        print(self.name,self.__hp,self.__ap,self.mt)

    def set_hp(self,value):
        if 0<=value<=100:
            self.__hp=value
        else:
            raise ValueError('hp')
    def get_hp(self):
        return self.__hp
    def set_ap(self,value):
        if 0<value<50:
            self.__ap=value
        else:
            raise ValueError('攻击力太高')
    def get_ap(self):
        return self.__ap

enemy01=Enemy('a',60,40,200)
enemy02=Enemy('b',70,45,200)
print(enemy01.get_ap())
enemy02.set_hp(20)
print(enemy02.get_hp())
