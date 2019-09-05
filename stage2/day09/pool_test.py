'''有大量事件，频繁创建进程会消耗系统资源
进程池实例（爬虫可能会用）'''
from multiprocessing import Pool
import time

# 进程池执行
def worker(msg):
    time.sleep(2)
    print(time.ctime(),'--',msg)

# 创建进程池 默认参数不写系统会自动分配（一般为内核数量）
pool1 = Pool()


# 添加事件
for i in range(10):
    msg = 'tedu %d'%i
    pool1.apply_async(worker,args=(msg,))
# 关闭进程池（不能再添加新事件了）
pool1.close()

# 回收进程池
pool1.join()
