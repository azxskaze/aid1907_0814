class StudentMode:
    def __init__(self, name='', age=0, score=0,id=0):
        self.name=name
        self.age=age
        self.score=score
        self.id = id
        '''
        def __str__(self)
            函数的作用是将对象的返回值变
            成用户自定义的字符串
            （自定义，可以自己拼接）
        '''
    def __str__(self):
        return '编号%s，姓名%s'%(self.id,self.name)
        '''把对象的返回值设置为字符串
        （解释器可以识别的）
        不可以自定义，有固定格式
        类名（字符串格式化）%字符串格式化'''
    def __repr__(self):
        return 'StudentMode("%s","%s","%s","%s")'%(self.name,self.age,self.score,self.id)

s01=StudentMode('a',1,2,3)
'''
    现在s01就是__str__方法的返回值
    而不是之前的存放对象的地址
    '''
print(s01)
s02=eval(repr(s01))
'''相当于克隆了一个s02出来，但是是深拷贝
s01和s02是两个属性相同的对象'''
'''返回python格式的字符串'''
print(s02)
s02.name='b'
print(s01)