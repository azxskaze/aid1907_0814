class Enemy:
    def __init__(self, name=None, hp=None, atk=None, mt=None):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.mt = mt
    def __str__(self):
        return '%s %s %s %s'%(self.name,self.hp,self.atk,self.mt)
enemy_list = [
    Enemy('灭霸',300,50,30),
    Enemy('布克', 180, 50, 20),
    Enemy('no1', 100, 50, 10),
    Enemy('no2', 0, 50, 25),
]
def find(list,func_condition):
    for i in list:
        if func_condition(i):
           yield i
def condition1(item):
    return item.hp<=0
# def back1(i):
#     return eval('return %s'%i)
# def back2(i):
#     return eval('yield (%s.name,%s.atk)'%(i,i))
a=''
def find_max(list):
    hp_max=0
    max=list[0]
    for i in list:
        if i.hp>hp_max:
            hp_max=i.hp
            max=i
    return max

def find_all(list):
    for i in list:
        yield (i.name,i.atk)

for i in find(enemy_list,condition1):
    print(i)
print(find_max(enemy_list))

for i in find_all(enemy_list):
    print(i)