# from game_2048.model import GameModel
import random

from model import Location


class GameCoreControllerl:
    def __init__(self):
        self.__map=[[0, 0, 0, 0],
           [0,0,0,0],
           [0, 0, 0, 0],
           [0, 0, 0, 0]
           ]
        self.__list_empty_location=[]
        # self.__list_info=self.mode
    @property
    def map(self):
        return self.__map

    def __num_add(self, list):
        for i in range(len(list)):
            for j in range(len(list[i]) - 1):
                if list[i][j] == list[i][j + 1]:
                    list[i][j] += list[i][j]
                    list[i][j + 1] = 0


    def __left_move(self, list):
        for i in range(len(list)):
            for j in list[i][::-1]:
                if j == 0:
                    list[i].remove(j)
                    list[i].append(0)


    def __daoxu(self, list):
        for i in range(len(list)):
            list01 = list[i][::-1]
            list[i] = list01

    def __zuozhuan(self, list):
        list01 = []
        for i in range(len(list)):
            list01.append([])
            for j in range(len(list[i])):
                list01[i].append(list[j][i])
        for i in range(len(list01)):
            list[i] = list01[len(list01) - 1 - i]

    def __youzhuan(self, list):
        list01 = []
        for i in range(len(list)):
            list01.append([])
            for j in range(len(list[i])):
                list01[i].append(list[j][i])
        for i in range(len(list01)):
            list[i] = list01[i][::-1]

    def zuoyixiangjia(self, list):
        self.__left_move(list)
        self.__num_add(list)
        self.__left_move(list)

    def youyixiangjia(self, list):
        self.__daoxu(list)
        self.zuoyixiangjia(list)
        self.__daoxu(list)

    def shangyixiangjia(self,list):
        self.__zuozhuan(list)
        self.zuoyixiangjia(list)
        self.__youzhuan(list)

    def xiayixiangjia(self,list):
        self.__youzhuan(list)
        self.zuoyixiangjia(list)
        self.__zuozhuan(list)

    def generate_new_number(self):
        self.__get_empty_location()
        loc = random.choice(self.__list_empty_location)
        self.__map[loc.r][loc.c]=self.__select_random_number()
    def __get_empty_location(self):
        self.__list_empty_location.clear()
        for r in range(len(self.__map)):
            for c in range(len(self.__map)):
                if self.__map[r][c]==0:
                    self.__list_empty_location.append(Location(r,c))

    def __select_random_number(self):
        return 4 if random.randint(0,9)==0 else 2
    def random_2_4(self):
        dict01={}
        for i in range(len(self.__map)):
            for j in range(len(self.__map[i])):
                if self.__map[i][j]==0:
                    dict01[i*4+j]=self.__map[i][j]
        list01=[key for key in dict01]
        proxy = random.choice(list01)
        if random.randint(0,9)>7:
            dict01[proxy]=4
        else:dict01[proxy]=2

        for i in range(len(self.__map)):
            for j in range(len(self.__map[i])):
                if i*4+j==proxy:
                    self.__map[i][j]=dict01[proxy]
a=GameCoreControllerl()
# a.random_2_4()
a.generate_new_number()
for i in a.map:
    print(i)



