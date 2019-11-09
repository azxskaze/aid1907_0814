'''把url地址放到列表'''
import time
import random
import redis
time.sleep(3)
r = redis.Redis(host='176.234.6.27',port='6379',db=0,password='123456')
url = 'http://app.mi.com/category/2#page={}'
for i in range(67):
    page_link = url.format(i)
    r.lpush('mistore:urls',page_link)
    time.sleep(random.randint(3,4))
print(r.lrange('mistore:urls',0,67))