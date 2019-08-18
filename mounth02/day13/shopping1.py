class ShangPinModel:
    def __init__(self,name,price,id=0):
        self.id=id
        self.name=name
        self.price=price
    def show(self):
        print(self.id,self.name,self.price)
class DingDanModel:
    def __init__(self,id,count):
        self.id=id
        self.count=count
    def show(self):
        print(self.id,self.count,end=' ')
class ShangPinControllay:
    __shang_pin_id=100
    def __init__(self):
        self.__shang_pin_info={ShangPinModel('倚天剑',10000,101),
                               ShangPinModel('屠龙刀',10000,102),
                               ShangPinModel('九阳神功',10000,103),
                               ShangPinModel('九阴白骨爪',9999,104),
                               ShangPinModel('乾坤大挪移',8888,105),
                               ShangPinModel('七伤拳',7777,106)}
        self.__shang_pin_ding_dan=[]
    @property
    def shang__pin_info(self):
        return self.__shang_pin_info

    @property
    def shang_pin_ding_dan(self):
        return self.__shang_pin_ding_dan
    def print_info(self):
        print('*' * 50)
        for item in self.__shang_pin_info:
            item.show()
        print('*' * 50)
    def create_order(self,id,count):
        for item in self.__shang_pin_info:
            if item.id==id:
                self.__shang_pin_ding_dan.append(DingDanModel(id, count))
                return True
        return False
    def print_order(self):
        for item in self.__shang_pin_ding_dan:
            item.show()
            for i in self.__shang_pin_info:
                if item.id==i.id:
                    print(item.count*i.price)
    def calc_total_price(self):
        zong_jia=0
        for order in self.__shang_pin_ding_dan:
            for item in self.__shang_pin_info:
                if order.id==item.id:
                    price1=item.price
                    zong_jia+=order.count*price1
        return zong_jia
    def pay(self,zong_jia,money):
        while True:

            if money >= zong_jia:
                self.__shang_pin_ding_dan.clear()
                return money - zong_jia
            else:
                return False
class ShoppingConsoleView:
    def __init__(self):
        self.view=ShangPinControllay(

        )
    def __display_meun(self):
        prompt = '''
************
商店
************
按1购买
按2结算
按q退出
************
                '''
        print(prompt)
    def __select_menu(self):
        item = input(':')
        if item == 'q':
            return False
        elif item == '1':
            self.__print_info()
            self.__create_order()
            return True
        elif item == '2':
            self.__print_order()
            self.__calc_total_price()
            zongjia = self.view.calc_total_price()
            self.__pay(zongjia)
            return True


    def menu(self):
        while True:
            self.__display_meun()
            if self.__select_menu():
                continue
            else:
                break

    def __print_info(self):
        self.view.print_info()
    def __create_order(self):

        while True:
            id=int(input('输入商品编号'))
            count=int(input('输入购买数量'))
            re=self.view.create_order(id,count)
            if re==True:
                print('添加成功')
                break
            else:
                print('编号不存在，请重新输入')
    def __print_order(self):
        self.view.print_order()
    def __calc_total_price(self):
        self.view.calc_total_price()
    def __pay(self,zongjia):
        while True:
            money=float(input('请输入金额：'))
            re=self.view.pay(zongjia,money)
            if re:
                print('购买成功，应找回%s'%re)
                break
            else:
                print('金额不足，请重新输入')

view=ShoppingConsoleView()
view.menu()










