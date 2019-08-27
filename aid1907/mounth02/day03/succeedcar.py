from succeed_1 import Car
class ElectraCar(Car):
    def __init__(self,name,speed,weight,num):
        super().__init__(name,speed,weight,num)
        super().top
mycar=ElectraCar('a',"b",'c',60)
mycar.add_num(20)
print(mycar.num)
