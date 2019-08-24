from day18.List_helper import ListHelper

class Skill:
    def __init__(self, id, name, atk, duration, aaa=None):

        self.id = id
        self.name=name
        self.atk = atk
        self.duration = duration
        self.aaa=aaa
    def __str__(self):
        return self.name
list01 = [
    Skill(101,'乾坤大挪移',8000,30),
    Skill(102, '九阳神功', 9000, 50),
    Skill(103, '九阴白骨爪', 5000, 10),
    Skill(104, '黑虎掏心', 9800, 40),
    Skill(105, '葵花宝典', 6000, 2)
]
# 1,2
print(ListHelper.find_sum(list01,lambda item:item.atk))
print(ListHelper.find_sum(list01,lambda item:item.duration))
3,4
for i in ListHelper.find_all(list01,lambda item:(item.name,item.duration)):
    print(i)
for i in ListHelper.find_all(list01,lambda item:(item.name,item.atk)):
    print(i)
# # 5
print(ListHelper.find_max(list01,lambda list,i:list[i].atk).name)
print(ListHelper.find_max2(list01,lambda i:i.duration).name)
# 6
ListHelper.ascending_order(list01, lambda i:i.atk)
for i in list01:
    print(i.name,i.atk)
# ListHelper.ascending_order(list01, lambda i:i.duration)
# for i in list01:
#     print(i.name,i.duration)
