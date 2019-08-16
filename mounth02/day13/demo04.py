'''
'''
''''

面向对象第三大特点：多态


'''

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
        type.transport()

    # 交通工具类 代表所有的具体的交通工具
class Vehicle:
    def transport(self):
        '''
        可以先定义一个抽象的行为（移动）
        由子类具体去形象化
        Car--run
        Airplane--fly
        '''
        pass
        #因为太抽象了，写不出具体的方法，
        # 所以pass就行，具体的行为是什么由子类再详细定义

class Car(Vehicle):
    def transport(self):
        print('走你～')

class Airplane(Vehicle):
    def transport(self):
        print('fly')

a01 = Airplane()
lz = Person('老张')
lz.go_to('东北',a01)
