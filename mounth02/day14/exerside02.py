class GraphicsProcessingUnit:
    def __init__(self):
        self.__graphics_list=[]
    @property
    def graphics_list(self):
        return self.__graphics_list

    def add_graphics(self,graphics):
        if isinstance(graphics,Graphics):
            self.__graphics_list.append(graphics)
        else:
            raise ValueError('目标图形不是继承自程序规定的Graphics类')

    def area(self):
        sum=0
        for i in self.__graphics_list:
            sum+=int(i.area())
        return sum


class Graphics:
    def area(self):

        raise NotImplementedError('次父类方法没有被重写')

class Rectangle(Graphics):
    def __init__(self,long,wide):
        self.long=long
        self.wide=wide
    def area(self):
        return self.long*self.wide

class Round(Graphics):
    def __init__(self,r):
        self.r=r
    def area(self):
        return 3.14*self.r**2
class Delta(Graphics):
    def __init__(self,):
        pass
    # def area(self):
    #     pass

d=Delta()
r=Round(5)
rt=Rectangle(10,20)
gp=GraphicsProcessingUnit()
gp.add_graphics(r)
gp.add_graphics(rt)
gp.add_graphics(d)
print(gp.area())
d=Delta()