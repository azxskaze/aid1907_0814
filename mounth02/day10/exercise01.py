class Dog:
    def __init__(self,name,kinds,color):
        self.name=name
        self.kinds=kinds
        self.color=color
    def eat(self,food):
        print('%s正在吃%s'%(self.name,food))
    def run(self,spend):
        print('%s正在以%skm/h的速度run'%(self.name,spend))
dog1=Dog('柴淳','秋田','white')

wangcai=Dog('旺财','中华田园犬','yellow')

dog1.eat('花椰菜')

wangcai.run(100)
print(dog1.__dict__,wangcai.__dict__)
doudou=wangcai
print(wangcai,doudou,sep='\n')

doudou.eat('火腿')
wangcai.eat('骨头')
doudou.name='豆豆'
'''
doudou=wangcai
doudou.name='豆豆'
相当于是浅拷贝，
别名对象对数据进行改变后
会作用到到原对象的数据上去'''

wangcai.eat('排骨')
list01=[wangcai,doudou,Dog('二哈','哈士奇','灰色')]
list02=list01
list02[2].color='白色'