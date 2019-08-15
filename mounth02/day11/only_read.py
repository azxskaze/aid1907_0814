"""age为只读"""
class Wife:
    def __init__(self,name,age):
        self.name = name
        self.age=age
    # @property
    def get_age(self):
        return self.__age
    # def set_age(self,value):
    #     self.__age=value
    age=property(get_age,None)

'''这样也行'''


w01=Wife('caster',25) #-->25读不进去的
w01.age=50
print(w01.age)  #-->20


