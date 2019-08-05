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