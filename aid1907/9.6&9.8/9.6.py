'''9.6'''
class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
    def describe_restsurant(self):
        print(self.restaurant_name,self.cuisine_type)
    def open_restaurant(self):
        print('open')

class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type):
        self.__flavors=['口味1','口味2']
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        # super().__init__(restaurant_name,cuisine_type)
    def show(self):
            for item in self.__flavors:
                print(item)
ice_1=IceCreamStand('ice','bigger')
ice_1.show()

