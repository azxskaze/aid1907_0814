class Person:
    def __init__(self, name):
        self.name = name
    def say(self):
        print('say')

class Student(Person):
    pass
    # def __init__(self,name):
    #     self.name=name

class Teacher(Person):
    # 若子类有构造函数 会覆盖父类的构造函数
    # 要想使用父类的构造善书中的属性
    # 必须先调用父类构造函数
    # super.__init__(父类中的属性1，父类中的属性1)
    def __init__(self,name,age):
        self.age=age
        super().__init__(name)


    # def __init__(self,name):
    #     self.name=name
s01 = Student('a')
s01.say()
t01=Teacher('a',18)
print(t01.name)


