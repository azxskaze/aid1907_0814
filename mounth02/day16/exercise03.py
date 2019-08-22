from day16.demo06 import AtkError


class Enemy:
    def __init__(self,atk):
        self.atk = atk
    @property
    def atk(self):
        return self.__atk
    @atk.setter
    def atk(self,value):
        try:
            if 0 <= value <= 100:
                self.__atk = value
            else:
                raise AtkError(1001,'0 <= value <= 100','攻击力异常')
        except AtkError as a:
            print(a)
if __name__ == '__main__':
    enemy01 = Enemy(99)


