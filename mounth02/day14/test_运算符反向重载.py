class Vector1:
    def __init__(self,x):
        self.x=x
        '''反向云算法，对象在数字的后面'''
    def __radd_(self,other):
        return Vector1(self.x+other)
        # '''符合运算，运用这种运算配合
        # v01+=other语句
        # 可以实现不改变原有对象进行加法操作'''
    def __iadd__(self, other):
        return Vector1(self.x+other)
    def __str__(self):

        return str(self.x)
v01=Vector1(10)
v01=v01+2
'''
写成v01=v01+2
时左边的v01和右边的v01不是一个对象
id（v01）！=id（v01）
'''
'''
默认使用__add__时会改变对象，
相当于v01=v01+2
在运算完之后，一般会产生新对象

'''
'''
用__iadd__  (重载符合运算)
v01+=2
实现在原对象基础上进行加法操作，
不会改变对象
'''
v01+=2