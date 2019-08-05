from succeed_2 import Car
class ElectraCar(Car):
    # __slots__ = (‘aaa’)
    '''限定一个类只有固定的实例变量‘aaa’
    加上之后，就不能在类的外面创建其他的实例变量了'''
    def __init__(self,name,speed,weight,num):
        super().__init__(name,speed,weight,num)
        super().show
    fnn=100
    __fn='私有变量'
    def __nume(self):
        print('私有方法')

    def numd(self):
        return  self.__nume()
    def get(self):
        return self.__fn
mycar=ElectraCar('a',"b",'c',60)
# mycar.add_num(20)
# print(mycar.num)

print(mycar.get())
'''通过类中的方法get()来访问类的私有变量__fn'''

mycar.numd()
'''通过类中的方法numd()来访问类的私有方法__nume()'''
print(ElectraCar.fnn)
'''通过类.变量名的方式可以直接访问实例变量'''
mycar.t=12
'''成员变量'''
mycar.r=32
'''成员变量'''
ElectraCar.i=150
'''类变量'''
ElectraCar.o=455
'''类变量'''
b=ElectraCar('f',"r",'g',70)

print(mycar.r,mycar.t)
print(b.i,b.o)
'''qizssss'''