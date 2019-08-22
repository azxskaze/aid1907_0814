import mode_test
'''这种方式导入模块可以
不用担心命名冲突
使用麻烦'''
# mode_test.A
# from mode_test import A as C

'''
from mode_test import A as C
将模块中的内容A改名为C'''
from mode_test import *
'''from mode_test import *
将模块中的所有内容导入当前文件
写起来很方便，结构很清晰，
但是可读性很差，
会把以一些不需要的东西假日进来
容易对模块中的内容进行误操作，改写'''
class C:
    def a(self):
        print('888')
class B(C):
    pass
b=B()
b.a()
b.c()
'''当前文件和模块中的命名相同时相当于改写模块内容'''