'''gevent 协程模块演示'''
import gevent

# 携程函数
def foo(a,b):
    print('Running foo')
    print(a,b)
    gevent.sleep(3)
    print('Foo again')

def foo2(a,b):
    print('Running foo2')
    print(a,b)
    gevent.sleep(3.1)
    print('Foo2 again')

# 生成协程对象
f = gevent.spawn(foo,1,2)
g = gevent.spawn(foo2,3,4)

gevent.joinall([f,g]) #阻塞等待 f 执行结束