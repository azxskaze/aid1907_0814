import random
game_bool = 1
list_info = [[0, 0, 0, 0],
           [0,0,0,0],
           [0, 0, 0, 0],
           [0, 0, 0, 0]
           ]
def random_2(list):
    dict01 = {}
    dict02={}
    array_dict(dict01, list)
    dict_dict2(dict01, dict02)
    loss(dict02)
    random_get(dict02)
    dict2_dict(dict01, dict02, list)

def dict2_dict(dict01, dict02, list):
    for k1 in dict01:
        for k2 in dict02:
            if k1 == k2:
                dict01[k1] = dict02[k2]
    for i in range(len(list)):
        for j in range(len(list[i])):
            list[i][j] = dict01[i * 4 + j]
            '''在0的位置随机生成2'''

def random_get(dict02):
    a1 = random.randint(0, len(dict02))
    while True:
        a2 = random.randint(0, len(dict02))
        if a1 != a2:
            break
    i = 0
    for k in dict02:
        if i in (a1, a2):
            dict02[k] = 2
        i += 1


def loss(dict02):
    if len(dict02) < 2:
        global game_bool
        game_bool = 0
        print('you loss')

def dict_dict2(dict01, dict02):
    # 将字典映射到另一个字典
    for k, v in dict01.items():
        if v == 0:
            dict02[k] = v

def array_dict(dict01, list):
    # 将矩阵映射到字典
    for i in range(len(list)):
        for j in range(len(list[i])):
            dict01[i * 4 + j] = list[i][j]

def zuoyixiangjia(list):
        left_move(list)
        num_add(list)
        left_move(list)

def num_add(list):
    for i in range(len(list)):
        for j in range(len(list[i]) - 1):
            if list[i][j] == list[i][j + 1]:
                list[i][j] += list[i][j]
                list[i][j + 1] = 0

def left_move(list):
    for i in range(len(list)):
        for j in list[i][::-1]:
            if j == 0:
                list[i].remove(j)
                list[i].append(0)

def daoxu(list):
    for i in range(len(list)):
        list01=list[i][::-1]
        list[i]=list01

def youyixiangjia(list):
    daoxu(list)
    zuoyixiangjia(list)
    daoxu(list)

def zuozhuan(list):
    list01=[]
    for i in range(len(list)):
        list01.append([])
        for j in range(len(list[i])):
            list01[i].append(list[j][i])
    for i in range(len(list01)):
        list[i]=list01[len(list01)-1-i]

def youzhuan(list):
    list01=[]
    for i in range(len(list)):
        list01.append([])
        for j in range(len(list[i])):
            list01[i].append(list[j][i])
    for i in range(len(list01)):
        list[i]=list01[i][::-1]

def shangyixiangjia(list):
    zuozhuan(list)
    zuoyixiangjia(list)
    youzhuan(list)

def xiayixiangjia(list):
    youzhuan(list)
    zuoyixiangjia(list)
    zuozhuan(list)

def show(list):
    """
游戏界面展示及最大数检测
    :param list:
    """
    global game_bool
    for i in range(len(list)):
        for j in range(len(list[i])):
            if list[i][j]>=2048:
                game_bool==2
                print('you win')
            print(str(list[i][j]).center(3),end=' ')
        print()
def game(list):
    """
游戏逻辑判断
    :param list:
    """
    key = input('请输入方向（wasd/上左下右）')
    if key=='a':
        zuoyixiangjia(list)
    elif key=='w':
        shangyixiangjia(list)
    elif key=='s':
        xiayixiangjia(list)
    else:
        youyixiangjia(list)

if __name__=='__main__':
    random_2(list_info)
    show(list_info)
    while True:
        if game_bool==0:
            break
        elif game_bool==2:
            print()
            break
        game(list_info)
        random_2(list_info)
        show(list_info)





















