class Car():
    def __init__(self,name,speed,weight):
        self.name=name
        self.speed=speed
        self.weight=weight
    def get_name(self):
        return self.__name
    def set_name(self,value):
        if value>10:
            self.__name=value
        else:
            raise RuntimeError('namexiaole')
    name=property(get_name,set_name)
    def get_speed(self):
        return self.__speed
    def set_speed(self, value):
        if value > 10:
            self.__speed = value
        else:
            raise RuntimeError('speedxiaole')
    speed = property(get_speed, set_speed)
    def get_weight(self):
        return self.__weight
    def set_weight(self, value):
        if value > 10:
            self.__weight = value
        else:
            raise RuntimeError('weightxiaole')
    weight = property(get_weight, set_weight)
car=Car(15,14,14)

# car.name=3
print(car.name)


