class Enemy:
    def __init__(self,name,hp,atk):
        self.name=name
        self.hp=hp
        self.atk=atk
    def __str__(self):
        return '名字：%s，血量：%s，攻击力：%s'%(self.name,self.hp,self.atk)
    def __repr__(self):
        return 'Enemy("%s",%d,%d)'%(self.name,self.hp,self.atk)
enemy=Enemy('a',2,5)
enemy02=eval(repr(enemy))

'''相当于是把enemy对象的属性拿出来重新创建了一个enemy02对象
深拷贝'''

print(enemy02)
enemy02.name='b'
print(enemy.name)
