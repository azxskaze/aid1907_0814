'''property版本2'''
class Enemy:

    def __init__(self, name, hp, ap, mt):
        self.name = name
        self.hp=hp
        self.ap=ap
        self.mt = mt

    def get_hp(self):
        return self.__hp

    def set_hp(self,value):
        if 0<value<100:
            self.__hp=value
        else:
            raise ValueError(1)
    '''拦截对hp的读写操作'''
    hp=property(get_hp,set_hp)
a=Enemy(1,100,1,2)
a.hp=500
print(a.hp)