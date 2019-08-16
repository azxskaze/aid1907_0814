'''继承语法'''
'''
多个子类在概念上一致时 考虑抽象出一个父类
多个子类中的共性提取到父类中
从设计的角度：  先有子类再有父类
写好子类，将子类中相同的部分根据需要写成父类
从编码角度：  先有父类再有子类'''
class Person:
    def say(self):
        print('aaaaa')

class Student(Person):
    # def __init__(self):

    def study(self):
        print('xuexi')

class Teacher(Person):

    def teach(self):
        print('shangke')
stu01=Student()
stu01.say()
'''子类可以直接调用父类成员，但是父类不能调用子类成员'''

print(isinstance(stu01,Person))
#isinstance 判断对象是否属于一个类
print(issubclass(Teacher,Person))
#issubclass 判断一个类是不是另一个类的子类

