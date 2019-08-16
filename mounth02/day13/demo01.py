'''继承'''
# __slots__ = (‘aaa’)
'''限定一个类只有固定的实例变量‘aaa’
加上之后，就不能在类的外面创建其他的实例变量了'''


class Student:
    def say(self):
        print('aaaaa')

    def study(self):
        print('bbbbb')

class Teacher:
    def say(self):
        print('aaaaaa')

    def teach(self):
        print('上课')
