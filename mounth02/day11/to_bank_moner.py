class Person:
    def __init__(self,name,money):
        self.name=name
        self.money=money
    def go_to(self,obj):
        print(self.name,'去',obj.name)
class Bank:
    def __init__(self,name,money):
        self.name=name
        self.money=money
    def withdraw_money(self,obj,amount):
        print('取钱')
        self.money-=amount
        obj.money+=amount
ming=Person('小明',10)
icbc=Bank('银行',100000000000)
ming.go_to(icbc)
icbc.withdraw_money(ming,100)


