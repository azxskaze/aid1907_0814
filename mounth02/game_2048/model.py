class Location:
    '''

    在2048游戏中，模型类里面存放的
    应该是每个数据的位置（r，c）

    '''
    def __init__(self,r,c):
        self.r = r
        self.c = c
class DirectionModel:
    """
        方向数据模型
        枚举  常量(命名全部大写)
    """
    # 在整数基础上，添加一个人容易识别的"标签"
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3

