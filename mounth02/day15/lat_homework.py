'''
将技能里面的每个效果单独放在一个类里面（很详细）
通过技能效果父类进行继承
'''
#技能系统
# 技能影响效果
class SkillImpactEffect:
    '''
    技能影响效果
    '''
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

    '''把方法都放在构造器里面，就可以在
    创建对象的时候自动执行这些代码，
    不需要额外调用'''
    # 在构造器里面保存构造文件
    def __init__(self,name):
        # 根据名字在构造文件里面找技能
        self.name=name
        self.__dict_skill_config=self.__loacd_config_file()
        # 保存配置文件
        self.__list_effect_object=self.__create_effect_object()
        # 保存创建好的效果对象

    # 技能释放器
    def __loacd_config_file(self):
        # 读配置文件
        return {
            '韦陀杵':['LowerDeffect(3,2)','CostSPEffect(10)','DamageEffect(200)'],

        }
    # 创建对象
    # 在字典中 根据技能名找到影响效果 实现
    def __create_effect_object(self):
        # 根据名字在构造文件里面找技能
        # __dict_skill_config是一个字典，名字是键，技能效果是值，保存在列表中
        list_effect_name=self.__dict_skill_config[self.name]
        # list_effect_name=['LowerDeffect(0.3,2.5)','CostSPEffect(20)','DamageEffect(200)']
        return  [eval(item) for item in list_effect_name]
        # 将列表中的技能效果通过eval函数转化成可执行代码，添加到新的列表中，将这个列表返回

    def genernate_skill(self):
        print('释放技能',self.name)
        # 调用列表里面的所有技能效果
        for item in self.__list_effect_object:
            item.impact()


skill01=SkillDeployer('韦陀杵')
skill01.genernate_skill()
# 调用方法



