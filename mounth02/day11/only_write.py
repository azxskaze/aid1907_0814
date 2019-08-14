'''只写'''
class Wife:
    def __init__(self,name,age):
        self.name = name
        self.__age=age
    # def get_age(self):
    #     return self.__age
    def set_age(self,age):
        self.__age=age
    age=property(None,set_age)
w01=Wife('caster',25)

# w01.set_age(268)
# print(w01.get_age())
print(w01.age)
w01.age=50
print(w01.age)
# -->不可读