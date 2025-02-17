"""
    迭代器

"""

class SkillIterator:
    """
        迭代器
    """

    def __init__(self,data):
        self.__target = data
        self.__index = -1

    def __next__(self):
        # 如果没有数据则抛出异常
        if self.__index >= len(self.__target)-1:
            raise StopIteration
        # 返回数据
        self.__index += 1
        return self.__target[self.__index]

class GraphicManager:
    """
        技能管理器     可迭代对象
    """
    def __init__(self):
        self.__skills = []
        self.i=-1

    def add_graphic(self, str_skill):
        self.__skills.append(str_skill)

    def __iter__(self):
        self.i+=1

        yield self.__skills[self.i]


manager = GraphicManager()
manager.add_graphic("圆形")
manager.add_graphic("矩形")
manager.add_graphic("三角形")

# 错误：manager必须是可迭代对象__iter__(),
# for item in manager:
#     print(item)
iterator = manager.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item)
    except StopIteration:
        break




