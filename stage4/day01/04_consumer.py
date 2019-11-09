import redis
r = redis.Redis(host='176.234.6.27',port='6379',db=0,password='123456')

while True:
    result = r.brpop('mistore:urls',4)
    if result:
        print('正在抓：',result[1].decode())
    else:
        print('success')
        break