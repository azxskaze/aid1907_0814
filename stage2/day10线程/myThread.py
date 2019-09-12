from threading import Thread
import time

class MyThread(Thread):
    # 该方法可以修改但是第7行不能传参数
    def __init__(self,target,args = (),kwargs = None):
        super().__init__()
        self.target = target
        self.args = args
        self.kwargs = kwargs
    def run(self):
        self.target(*self.args,**self.kwargs)

# 测试函数，函数名称，参数都不确定，只是提供测试
def player(sec,song):
    for i in range(3):
        print('playing %s: %s'%(song,sec))
        print(time.ctime())

t = MyThread(target=player,args=(3,),kwargs = {'song':'song1'})
t.start()
t.join()