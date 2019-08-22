class ObjectModel:
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

class EnemyDeployer:

    def __init__(self):
        self.__list_enemy = self.__list_enemy()

        self.__list_enemy_obj = self.__create_enemy_object()

    def __loacd_config_file(self):
        return {
            '韦陀杵': ['LowerDeffect(3,2)', 'CostSPEffect(10)', 'DamageEffect(200)']}





class SkillImpactEffect:
    def impact(self):
        pass
# 伤害效果
class DamageEffect(SkillImpactEffect):
    def __init__(self,value):
        self.value=value
    def impact(self):
        print()


# 消耗法力
class CostSPEffect(SkillImpactEffect):
    def __init__(self,hp):
        self.hp=hp
    def impact(self):
        print('消耗法力',self.hp)
# 降低防御力
class LowerDeffect(SkillImpactEffect):
    def __init__(self,ratio,time):
        self.ratio=ratio
        self.time=time
    def impact(self):
        print('降低防御力',self.ratio)


class SkillDeployer:


    # 在构造器里面保存构造文件
    def __init__(self,name):

        self.name=name
        self.__dict_skill_config=self.__loacd_config_file()

        self.__list_effect_object=self.__create_effect_object()

    def __loacd_config_file(self):

        return {
            '韦陀杵':['LowerDeffect(3,2)','CostSPEffect(10)','DamageEffect(200)'],

        }

    def __create_effect_object(self):

        list_effect_name=self.__dict_skill_config[self.name]

        return  [eval(item) for item in list_effect_name]


    def genernate_skill(self):
        print('释放技能',self.name)

        for item in self.__list_effect_object:
            item.impact()


skill01=SkillDeployer('韦陀杵')
skill01.genernate_skill()




