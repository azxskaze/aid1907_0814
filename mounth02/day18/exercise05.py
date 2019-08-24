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

for i in ListHelper.find_all(list01,lambda i:(i.name,i.atk,i.duration)):
    print(i)
for i in map(lambda i:(i.name,i.atk,i.duration),list01):
    print(i)
# print(ListHelper.find_min(list01,lambda i:i.atk).name)
# print(min(list01,key = lambda i:i.atk))
# ListHelper.descending_order(list01,lambda i:i.duration)
# for i in list01:
#     print(i.name)
#
# for i in sorted(list01,key= lambda i:i.duration,reverse= True):
#     print(i.name)
#
#
# tuplu01=([1,1],[2,2,2,2,],[3,3])
# # print(max(tuplu01,key = lambda i:len(i)))
# print(ListHelper.find_max(tuplu01,lambda i:len(i)))
ListHelper.delete_obj(list01,lambda i:i.atk,6100)
for i in list01:
    print(i.atk)