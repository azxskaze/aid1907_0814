from day16.demo06 import AgeError
class Wife:
    def __init__(self,age):
        self.age=age
    @property
    def age(self):
        raise self.__age

    @age.setter
    def age(self, value):
        try:
            if 23 <= value <= 30:
                self.__age = value
            else:
                raise AgeError('不要奥', '23<=value<=30', '10101')
        except AgeError as e:
            print(e)

if __name__=='__main__':
    wife=Wife(22)
    

