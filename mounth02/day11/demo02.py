'''property
属性来控制输出
'''
class Wife:
    def __init__(self,name,age):
        self.name = name
        self.age=age
    def get_age(self):
        return self.age
    def set_age(self,age):
        self.age=age
    property=(get_age,set_age)
w01=Wife('caster',25)
w01.set_age(268)
print(w01.age)
