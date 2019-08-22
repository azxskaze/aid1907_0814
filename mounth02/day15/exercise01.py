# import model02
# model02.my_fun()
# m01=model02.MyClass02('aaaaa')
# m01.fun02()
# model02.MyClass02.fun03()

# from model02 import my_fun,MyClass02
#
# my_fun()
# m01=MyClass02('aaaaa')
# m01.fun02()
# MyClass02.fun03()
from model02 import *
my_fun()
m01=MyClass02('aaaaa')
print(m01.a)
m01.fun02()
MyClass02.fun03()