'''alt+enter创建新属性'''
'''  



类与类之间进行组合
今天的第一个重点



'''
class LittlePony:
    def __init__(self,size,color):

        self.size=size
        self.color=color

        '''类与类之间的组合'''
        # 面向对象组合，将两个类组合到一起，
        # 通过一个类可以调用两个累的属性
        self.vendor=Vendor()
    @property
    def size(self):

        return self.__size

    @size.setter
    def size(self, value):

        if value in ('little','meddie'):
            self.__size=value


    def sing(self):
        print('lalala')
    def speak(self):
        print('hola')
class Vendor:
    def __init__(self, phone='400-123-1212', address='莆田', email='@163.com'):
        self.email=email
        self.phone=phone
        self.address=address
    def call(self):
        # if obj.vendor==self
            print('给%s打call'%self.phone)
mylittlepony=LittlePony('little','white')
mylittlepony.vendor.call()