
class Skill:
    def __init__(self, id, name, atk, duration):

        self.id = id
        self.name=name
        self.atk = atk
        self.duration = duration
    def __str__(self):
        return self.name
list01 = [
    Skill(101,'乾坤大挪移',8000,30),
    Skill(102, '九阳神功', 9000, 50),
    Skill(103, '九阴白骨爪', 5000, 10),
    Skill(104, '黑虎掏心', 9800, 40),
    Skill(105, '葵花宝典', 6000, 2)
]


def condition01(item): 
    return item.duration>10
def condition02(item):
    return 102<=item.id<=105
def find(fun):
    for i in list01:
        if fun(i):
            yield i
for i in find(condition01):
    print(i)
for i in find(condition02):
    print(i)