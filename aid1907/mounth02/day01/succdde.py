class Car():
    def __init__(self,name,speed,weight,num):
        self.name=name
        self.speed=speed
        self.weight=weight
        self.num=num
    def show(self):
        print(self.name)
    def add_num(self,value):
        self.num+=value
class Mycar(Car):
    def __init__(self,name,speed,weight,num,day):
        super().__init__(name,speed,weight,num)
        self.day=day
    def time(self):
        self.day+=20
        return self.day
mycar=Mycar('a','23','2','32',90)
print(mycar.day)
print(mycar.time())

