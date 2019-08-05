class Car():
    def __init__(self,name,speed,weight):
        self.name=name
        self.speed=speed
        self.weight=weight

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,value):
        if value>10:
            self.__name=value
        else:
            raise RuntimeError('xiaole')

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        if value > 10:
            self.__speed = value
        else:
            raise RuntimeError('xiaole')

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, value):
        if value > 10:
            self.__weight = value
        else:
            raise RuntimeError('xiaole')
car=Car(12,15,14)
print(car.name)
car.name=3
print(car.name)


