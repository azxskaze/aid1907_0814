class Enemy:
    def __init__(self,name,health,mp,ap,mt):
        self.name=name
        self.health=health
        self.mp=mp
        self.ap=ap
        self.mt=mt

list_enemy=[Enemy('灭霸',10000,100,10000,10000),
            Enemy('洛基',1000,100,1500,5),
            Enemy('奥创',2000,120,1500,1000),
            Enemy('jockr',2000,200,500,500)]
def find(name):
    for i in list_enemy:
        if i.name==name:
            return i

def find_die():
    list01=[]
    for i in list_enemy:
        if i.health <= 0:
            list01.append(i)
    return list01
def avg_ap():
    sum=0
    for i in list_enemy:
        sum+=i.ap
    return (sum/len(list_enemy))

def del_die():
    for i in list_enemy:
        if i.mt <= 10:
            list_enemy.remove(i)
def add_ap():
    for i in list_enemy:
        i.ap+=50
print(find('灭霸').name)

list01=find_die()
for i in list01:
    print(i.name)
print('*',avg_ap())

avg_ap()
for i in list_enemy:
    print(i.ap)








