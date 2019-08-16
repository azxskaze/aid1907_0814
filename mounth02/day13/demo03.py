class Person:
    def __init__(self,name):
        self.name = name

    def go_to(self,position,type):
        '''
        :param position:地名
        :param type: 去的方法
        :return:
        '''
        print('去：'+position)
        '''这样做的话会违背设计的开闭原则'''
        if isinstance(type,Car):
            type.run()
        else:
            type.fly()

class Car:
    def run(self):
        print('走你～')
class Airplane():
    def fly(self):
        print('fly')
a01 = Airplane()
lz = Person('老张')
lz.go_to('东北',a01)
