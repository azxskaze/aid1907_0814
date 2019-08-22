class Target:
    # def __init__(self):
    #     pass
    def injury(self):
        pass

class Enemy():
    def injury(self):
        print('敌人hp-10')

class Player():
    def injury(self):
        print('玩家hp-5')

# class Uknow(Target):
#     pass
# class Plan(Uknow):
#     print('')
# class Toy(Uknow):
#     def injury(self):
#         print('')
# class Damageable:
#     def injury(self):
#         '''如果子类不重写就抛出异常'''
#         raise NotImplementedError()
# class A(Target):
#     def __init__(self):
#         super().__init__()
#     pass


class Grenade:
    def boom(self,obj):
        # if not isinstance(obj,Target):
        #     print('不可受伤目标')
        #     return 0
        obj.injury()
        # print('boom')
enemy=Enemy()
player=Player()
# toy=Toy()
# tree=Plan()
g=Grenade()
# a=A()

g.boom(enemy)
# g.boom(tree)

g.boom(player)

# g.boom(toy)
# g.boom(a)


