''''''

'''
变量作用域
L（local）：局部做用域（函数内部），局部变量
当函数调用时，创建局部变量，函数结束时销毁
E（enclosing）：（上一级函数）外部嵌套作用域
G（global）：全局作用域,文件内都可以访问到
B（built-in）：内置作用域，系统模块定义的变量
L>E>G>B
'''

a=100
def change():
    a=10
    def in1():
        a=1
        print(a)
    in1()
    print(a)
change()
print(a)

