import redis
from multiprocessing import Process
import time
import random
class XiaomiSpider:
    def __init__(self):
        self.r = redis.Redis(host='176.234.6.27',port='6379',db=0,password='123456')
    # 消费者进程事件函数
    def consumer(self):
        while True:
            result = self.r.brpop('mistore:urls', 4)
            if result:
                print('正在抓：', result[1].decode())
            else:
                print('success')
                break
    # 生产者进程事件函数
    def produce(self):
        url = 'http://app.mi.com/category/2#page={}'
        for i in range(67):
            page_link = url.format(i)
            self.r.lpush('mistore:urls', page_link)
            time.sleep(random.randint(1,3))
    # 入口函数
    def run(self):
        p1 = Process(target=self.produce)
        p2 = Process(target=self.consumer)
        # p1.daemon = True
        # p2.daemon = True
        p1.start()
        p2.start()
        p1.join()
        p2.join()

if __name__ == '__main__':
    spider = XiaomiSpider()
    spider.run()