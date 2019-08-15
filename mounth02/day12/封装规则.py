'''

通常把既有数据
又有行为的物体创建为一类
只有数据没有行为的物体一般不创建为类
只当成数据

'''
# 老张开车去东北
class Person:
    def __init__(self,name):
        self.name=name
    def go_to(self,position,car=None):
        print(self.name,'去',position)
        # Car.run()
        # '''直接这样写的话耦合性太高了'''
        if car:
            car.run()
        else:
            print('走')
class Car:
    def __init__(self):
        pass
    def run(self):
        print('想去哪就去哪')
lz=Person('老张')
car=Car()
lz.go_to('东北')