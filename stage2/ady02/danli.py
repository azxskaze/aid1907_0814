class Earth(object):
    __instance = None  # 定义一个类属性做判断

    def __new__(cls):

        if cls.__instance == None:
            # 如果__instance为空证明是第一次创建实例
            # 通过父类的__new__(cls)创建实例
            cls.__instance = object.__new__(cls)
            return cls.__instance
        else:
            # 返回上一个对象的引用
            return cls.__instance

a = Earth()
print(id(a))
b = Earth()
print(id(b))
