class Skill:
    def __init__(self,name,faction):

        self.faction=faction
        self.name = name

    def description(self):
        pass

class ConsumeSkill(Skill):
    def __init__(self,name,consume,cd,faction):
        super().__init__(name,faction)
        self.consume = consume
        self.cd = cd

    def description(self):
        pass

class Player:
    def __init__(self,name,faction,hp,mp,atk,mt,x,y,speed,attack_distance):
        self.name = name
        self.faction = faction
        self.hp = hp
        self.mp=mp
        self.atk=atk
        self.mt=mt
        self.x=x
        self.y=y
        self.speed=speed
        self.attack_distance=attack_distance

 # 施加对象距离：6码单个近身  4码范围内所有 4步范围内所有
# # 5步范围内所有 4码范围内所有 前方5步 7步范围内单个
# # 选中区域内所有 前方7码 8码范围内所有 全屏
#
# # 对敌人效果：造成伤害100% 120% 200%
#
# # 减速30% 50% 嘲讽 眩晕 拉扯 沉默 冻结 降低防御力
# # 对友方效果 贾少伤害 攻击力提升
#
class ControlFunction:#功能类（按照技能里面的功能进行拆解）
    def __init__(self,play):

        self.play=play #玩家属性
        self.__skill_list=[]#技能列表
        self.__enemy_list=[]#敌人列表

    @property
    def skill_list(self):
        return self.__skill_list
    def learn_skill(self,skill):#学习技能
        if skill.faction==self.play.faction:
            self.__skill_list.append(skill)
        print(len(self.__skill_list))

    # def release_skill(self,key):#释放技能
    #     self.__skill_list[key].description()

    def enemy_list(self,enemy):#添加敌人
        if enemy:
            self.__enemy_list.append(enemy)
    def dist(self,enemy):#计算距离
        return (self.play.x-enemy.x)**2+(self.play.y-enemy.y)
    #计算最小距离的敌人
    def dist_min(self):
        atk_list = []
        min=self.dist(self.__enemy_list[0])
        min_i=self.__enemy_list[0]
        for i in self.__enemy_list:
            if self.dist(i)<min:
                min=self.dist(i)
                min_i=i
        atk_list.append(min_i)
        return atk_list
    #计算指定范围内的敌人
    def dist_distance(self,distance):
        atk_list=[]
        for i in self.__enemy_list:
            if self.dist(i)<=distance**2:
                atk_list.append(i)
        return atk_list

# 查找敌人可以单做一系列类




class view:
    def __init__(self,player):
        self.control=Control(player)

pass




class LuoHanGun(ConsumeSkill):

    def __init__(self,name,faction,consume,cd):
        super().__init__(name,faction,consume,cd)
        self.control=Control(player)
        self.player=self.control.play
    def description(self):
        print(self.name)
        self.control.dist_min().hp-=(self.control.play.atk)*2


player=Player('a','少林',1000,500,100,100,50,100,200,200)
player2=Player('a','少林',1020,400,200,100,100,120,100,100)
c=Control(player)
c.enemy_list(player2)
c.learn_skill(LuoHanGun('罗汉棍','少林',10,10))

c.release_skill(0)








# # 施加对象距离：6码单个近身  4码范围内所有 4步范围内所有
# # 5步范围内所有 4码范围内所有 前方5步 7步范围内单个
# # 选中区域内所有 前方7码 8码范围内所有 全屏
#
# # 对敌人效果：造成伤害100% 120% 200%
#
# # 减速30% 50% 嘲讽 眩晕 拉扯 沉默 冻结 降低防御力
# # 对友方效果 贾少伤害 攻击力提升
#
# # class
# class Person:
#     def __init__(self,profession,name,hp,mp,speed,atk,mt):
#         self.profession=profession
#         self.name=name
#         self.hp=hp
#         self.mp=mp
#         self.speed=speed
#         self.atk=atk
#         self.mt=mt
#
# class Individual(Skill):
#     def __init__(self,profession,name,mp,cd,distance,damage):
#         self.distance=distance
#         self.damage=damage
#         super().__init__(profession,name,mp,cd)
#     def description(self):
#
#         pass


# str01='1 23'
# l=str01.split(' ')
# print(l)
# list02=[]
# list02.append(l[1][::-1])
# list02.append(l[0][::-1])
#
# print(list02)
# str02=' '.join(list02)
# print(str02)
# str01='welcome to beijing'
# list01=str01.split(' ')
# list02=[]
# for item in list01:
# 	list02.append(item[::-1])
# str02=' '.join(list02)
# print(str02)


# while True:
# 	for item in range(3):
# 		name = input('p')
# 		if name ==  'tarena':
# 			break
# 		else:
# 			print(2)
# 	else:
# 		print(5)
# 		break
# 	for item in range(3):
# 		name = input(3)
# 		if name ==  '123456':
# 			break
# 		else:
# 			print('2')
# 	else:
# 		print('次数超限')
# 		break
# 	print(1)
a='ABCD\'EFG'
print(a[0:-1:-1])

































# class ShaoLinSkill(Skill):
#     def __init__(self,profession,name,mp,cd):
#         self.profession='少林'
#         super().__init__(name,mp,cd)
#     def description(self):
#         pass
#
# class XiaoYaoSkill(Skill):
#     def __init__(self,profession,name):
#         self.profession='逍遥'
#
#         super().__init__(name)
#     def description(self):
#         pass
#
# class GaiBangSkill(Skill):
#     def __init__(self,profession,name,mp,cd):
#         self.profession='丐帮'
#
#         super().__init__(name,mp,cd)
#     def description(self):
#         pass
#
# class profession:
#     def __init__(self,name):
#         self.name=name