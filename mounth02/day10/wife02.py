class Wife:
    pass
w01 = Wife()
w01.name='托尔'
w02=Wife()
print(w01.__dict__)
'''可以通过__dict__
获取当前对象的所有实例变量'''
# print(w02.name)#会报错，因为w02没有定义name

class Wife2:
    def __init__(self,name,age):
        '''构造函数 添加实例变量（属性）'''
        self.name=name
        self.age=age
    def print_self(self):
        '''构造函数 添加实例方法'''
        print(self.name)
        print(self.age)
wi01=Wife2('艾米莉亚',20)

wi01.print_self()
'''一般用对象.方法进行调用'''
Wife2.print_self(wi01)
'''也可以通过类.方法（对象）
进行调用但不建议（禁用）
其他语言不支持这样调用'''
print(wi01.__dict__)
