class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
    def describe_restsurant(self):
        print(self.restaurant_name,self.cuisine_type)
    def open_restaurant(self):
        print('open')

class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type,*flavors):
        self.flavors=flavors
        # self.restaurant_name = restaurant_name
        # self.cuisine_type = cuisine_type
        super().__init__(restaurant_name,cuisine_type)
    def show(self):

            print(self.flavors,self.restaurant_name,self.cuisine_type)
ice_1=IceCreamStand('ice','bigger',1,2,3)
ice_1.show()

