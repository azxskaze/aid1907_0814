'''运算符重载'''
class Vector1:
    def __init__(self,x):
        self.x=x
# '''正向运算符重载，对象必须在数字的前面'''
    def __add__(self, other):
        return  Vector1(self.x-other)

    def __sub__(self, other):
        return  Vector1(self.x+other)
    def __mul__(self, other):
        return  Vector1(self.x/other)
    def __divmod__(self, other):
        return Vector1(self.x+other)
    def __str__(self):
        return  str(self.x)
v01=Vector1(10)
print(v01+2)
'''已经把加法重载为减法了'''
print(v01-2)
'''已经把减法重载为加法了'''
print(v01*2)
'''已经把乘法重载为除法了'''
print(v01%2)
