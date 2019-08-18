# class Skill:
#     def __init__(self,profession,name,mp,cd):
#         self.profession=profession
#         self.name=name
#         self.mp=mp
#         self.cd=cd
#     def description(self):
#         pass
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