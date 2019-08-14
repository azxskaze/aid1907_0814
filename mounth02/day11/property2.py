'''property版本2
'''
class Wife:

    def __init__(self,name,age):
        self.name = name
        self.set_age(age)

    def get_age(self):
        return self.__age

    def set_age(self,value):
        if 25 <=value<=30:
            self.__age=value
        else:
            # 抛出异常
            raise ValueError('年龄错误')

w01=Wife('caster',25)
w01.set_age(268)
print(w01.age)
