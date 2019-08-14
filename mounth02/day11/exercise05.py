'''老张开车去东北'''
class Person:
    def __init__(self,name):
        self.name=name
    def move(self,type,car):
        print(self.name,'开着',car,'去',type)

class Car:
    def __init__(self,size):
        self.size=size
lz=Person('老张')
car=Car('汽车')
# print(people.name,people.move,car.size,'去东北')
lz.move('东北',car.size)
