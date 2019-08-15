class Stor:
    __gou_wu_che = {}

    def __init__(self):
        self.__shnag_pin_info={
    101: {'name': '倚天剑', 'price': 10000},
    102: {'name': '屠龙刀', 'price': 10000},
    103: {'name': '九阳神功', 'price': 10000},
    104: {'name': '九阴白骨爪', 'price': 9999},
    105: {'name': '乾坤大挪移', 'price': 8888},
    106: {'name': '七伤拳', 'price': 7777}
}

    @property
    def shnag_pin_info(self):
        return self.__shnag_pin_info

    def __buying(self):
        count = int(input('请输入商品编号'))
        while True:
            if count not in self.__shnag_pin_info:
                print('商品不存在')
            else:
                if count in Stor.__gou_wu_che:
                    Stor.__gou_wu_che[count][0] += 1
                else:
                    list01 = []
                    list01.append(1)
                    list01.append(self.__shnag_pin_info[count]['price'])
                    Stor.__gou_wu_che[count] = list01
                print('添加到购物车')
                break

    def __paying(self):
        sum = 0
        for key in Stor.__gou_wu_che:
            sum += float(Stor.__gou_wu_che[key][0]) * float(Stor.__gou_wu_che[key][1])
        print('')

        while True:
            money = float(input('请输入金额：'))
            if money < sum:
                print('金额不足')
            else:
                print('应找回%.1f' % (money - sum))
                Stor.__gou_wu_che.clear()
                break

    def menu(self):
        while True:
            print('*'*12,'\n','商店','\n','*'*12,'\n','按1购买\n按2结算','\n','*'*12,sep='')

            key=int(input(':'))

            if key==1:
                self.__show()
                self.__buying()
            elif key==2:
                print('*'*12,'\n','购物车','\n','*'*12,sep='')
                self.__show_gou_wu_che()
                self.__paying()
            else:
                break

    def __show_gou_wu_che(self):
        for key in Stor.__gou_wu_che:
            print(key, end=' ')
            for i in Stor.__gou_wu_che[key]:
                print(i, end=' ')
            print()

    def __show(self):
        for k, v in self.__shnag_pin_info.items():
            print(k, end=' ')
            for i in v.values():
                print(i, end=' ')
            print()

stor01=Stor()
stor01.menu()
