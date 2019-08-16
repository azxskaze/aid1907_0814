class Animal:
    def shout(self):
        print('call')
    def eat(self):
        print('eatting')

class Dog(Animal):
    # def shout(self):
    #     print('wangwang')
    def run(self):
        print('runing')

class Brid(Animal):
    # def shout(self):
    #     print('zhazha')
    def fly(self):
        print('flying')

dog=Dog()
brid=Brid()
animal=Animal()
# 体会一下三种方法的区别
print(isinstance(brid,Animal))
# 判断是否为这个类或者是这个类的子类的对象

print(issubclass(Dog,Animal))
# 判断是否为这个类的子类
print(isinstance(dog,Animal))#-->True(dog属于Animal类)
print(type(dog)==Animal)
# 判断这个对象是否是由这个类所直接创建的
#-->False (dog对象不是Animal类，
# 只是Animal的一个子类创建的对象# )
