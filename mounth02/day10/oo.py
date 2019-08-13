'''类与类之间行为不同
    对象与对象之间数据不同'''
class Wife():
    # 数据成员：
    # 身高 体重 姓名
    def __init__(self,height,weight,name='shiki'):
        '''
        __init__
            相当于C语言中的构造函数，
            作用是给实例对象赋值
        在创建对象时会自动调用
        '''
        self.height=height
        self.weight=weight
        self.name=name
        '''self
        是表示当前对象的名称（可以自定义但不会这样做）
        相当于JAVA中的this
        '''
    def mo_tou(self):
        print('%s is singing'%self.name)
    def play_game(self,game):
        print('%s has playing %s'%(self.name,game))
    # 行为成员：

    # 唱歌
    #
    pass
shiki=Wife(154, name='兩儀', weight=45)
print(shiki.weight)
print(shiki.height)
print(shiki.name)
shiki.mo_tou()

quuen=Wife(154,54,'莉雅')
quuen.mo_tou()
quuen.play_game('over watch')



