class Enemy:
    def __init__(self, name, health, mp, ap, mt):
        self.name = name
        self.health = health
        self.mp = mp
        self.ap = ap
        self.mt = mt
    def show_enemy(self):
        print(self.name,self.health,self.mp,self.ap,self.mt)


list_enemy = [Enemy('灭霸', 10000, 100, 10000, 10000),
              Enemy('洛基', 100, 10, 150, 5),
              Enemy('奥创', 200, 12, 150, 10),
              Enemy('jockr', 200, 20, 50, 50)]


def find(name):
    for i in list_enemy:
        if i.name == name:
            return i


def find_die():
    list01 = []
    for i in list_enemy:
        if i.health <= 0:
            list01.append(i)
    return list01


def avg_ap():
    sum = 0
    for i in list_enemy:
        sum += i.ap
    return (sum / len(list_enemy))


# def del_die():
#     for i in list_enemy[::-1]:
#         if i.mt <= 10:
#             list_enemy.remove(i)
def del_die():
    for i in range(len(list_enemy)-1,-1,-1):
        if list_enemy[i]<10:
            del list_enemy[i]

def add_ap():
    for i in list_enemy:
        i.ap += 50


print(find('灭霸').name)

list01 = find_die()
for i in list01:
    print(i.name)
print('*', avg_ap())

add_ap()
for i in list_enemy:
    print(i.ap)
