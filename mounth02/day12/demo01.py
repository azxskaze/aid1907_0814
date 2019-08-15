'''

使用组合来解决

'''
# 老张开车去东北
class Person:
    def __init__(self,name):
        self.name=name
        self.car=Car(self.name)
        '''
        
        有耦合性，但是有必要耦合的时候
        可以适当进行耦合
        
        '''
    def go_to(self,position,type):
        print(self.name,'去',position)
        type.run()
        # Car.run()
        # '''直接这样写的话耦合性太高了'''


class Car:
    def __init__(self, ovner):
        self.ovner=ovner
    def run(self):
        print(self.ovner,'的车想去哪就去哪')
lz=Person('老张')
ll=Person('老李')
ll.go_to('东北',lz.car)