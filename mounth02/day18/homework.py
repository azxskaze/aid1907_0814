import time
def comput_time(fun):
    def warp(*args,**kwargs):
        a=time.time()
        fun(*args,**kwargs)
        b=time.time()
        print(b-a)
    return warp
@comput_time
def fun1():
    print('fun1')
fun1()
