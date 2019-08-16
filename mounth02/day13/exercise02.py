class Car:
    def __init__(self,brand,speed):
        self.brand=brand
        self.speed=speed
    def run(self):
        print('run')
class Electric_Car(Car):
    '''虽然调用的是Car的brand，speed但是，这两个属性
    在调用后的实例是属于Electric_Car类的
      print(type(e01)==Car)#-->False
      print(type(e01)==Electric_Car)#-->True
    '''
    def __init__(self,brand,speed,battery_capacity):
        self.battery_capacity=battery_capacity
        super().__init__(brand,speed)
e01=Electric_Car('特斯拉',120,3000)
e01.run()
print(type(e01)==Car)#-->False
print(type(e01)==Electric_Car)#-->True