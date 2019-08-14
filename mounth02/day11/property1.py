'''第一个版本
通过'__'创建私有变量
__age然后再定义两个方法，
一个获取__age,get_age
一个设置__age,set_age
'''
'''但是这种方法age就变成类的私有变量 
，对象不能接触，要读取和修改age只能通过类中的方法'''
class Wife:
    def __init__(self,name,age):
        self.name = name
        self.__age=age
    def get_age(self):
        return self.__age
    def set_age(self,age):
        self.__age=age
    # age=property(get_age,set_age)
w01=Wife('caster',25)
w01.set_age(268)
print(w01.get_age())
