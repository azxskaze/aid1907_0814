from day18.List_helper import ListHelper


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
def condition1(item):
    return item.id==102
def condition2(item):
    return item.name=='九阳神功'
# print(ListHelper.find_single(list01, condition1))
# print(ListHelper.find_single(list01, condition2))


print(ListHelper.find_single(list01, lambda item: item.id == 101))
print(ListHelper.find_single(list01, lambda item: item.name == '九阳神功'))
for i in ListHelper.find_all(list01,lambda item:True):
    print(i)
