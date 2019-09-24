
'''
自定义进程类
'''

from multiprocessing import Process
class MyProcess(Process):

    def __init__(self, value=None):
        self.value = value
        super().__init__()

    def f1(self):
        print('111111')
    def f2(self):
        print('22222222')
    def f3(self):
        print('3333333333')
    def run(self):
        self.f1()
        self.f2()
        self.f3()
p = MyProcess(2)
p.start()#执行run（）
p.join()
