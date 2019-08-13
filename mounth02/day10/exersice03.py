class Wife:
    num=0
    @classmethod
    def show_num(cls):
        print('%s'%cls.num)

    def __init__(self,name):
        self.name=name
        Wife.num+=1

w1=Wife('莜')
w1=Wife('咲')
w1=Wife('凛')
Wife.show_num()