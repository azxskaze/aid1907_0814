class ICBC:
    # 类方法
    # 实例对象也可以访问类方法但是不建议（其他语言不适用）
    @classmethod
    def select_moner(cls):
        '''cls保存当前类的地址
        cls就是类（ICBC）
        可以用类名.方法名()的方式调用
        可以用对象名.方法名()的方式调用（其他语言不通用，所以不建议）'''
        print(id(cls),id(ICBC))
        print(cls.total_money)
    # 总行的钱
    # 类变量
    total_money=1000000

    def __init__(self,name,money):
        self.name=name
        self.money=money
        ICBC.total_money-=money
        '''操作类中的数据，不要用实例方法'''
        # 实例方法
    # def select_money(self):
    #     print(ICBC.total_money)



i01=ICBC('碑林支行',100000)
i02=ICBC('雁塔支行',100000)
# print(ICBC.total_money)
# i01.select_money()

ICBC.select_moner()
i01.select_moner()
