'''最终版本'''
class Enemy:

    def __init__(self, name, hp, ap, mt):
        self.name = name
        self.hp=hp
        self.ap=ap
        self.mt = mt
    @property
    def hp(self):
        return self.__hp
    @hp.setter
    def hp(self,value):
        if 0<value<100:
            self.__hp=value
        else:
            raise ValueError(1)
a=Enemy(1,10,1,2)
print(a.hp)
a.hp=50
print(a.hp)
'''查看对象a的所有成员对应的字典'''
print(a.__dict__)
print(a._Enemy__hp)
'''可以通过对象._类名__hp
访问私有变量'''
