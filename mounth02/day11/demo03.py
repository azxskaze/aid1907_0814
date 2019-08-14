class Wife:
    def __init__(self,name,age):
        self.name = name
        # 私有成员：以下划线开头
        self.__age=age
w01 = Wife('rider',25)
# 私有变量不能通过对象进行访问
print(w01.age)