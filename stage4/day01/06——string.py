import redis
r = redis.Redis(host='176.234.6.27',port='6379',db=0,password='123456')

r.set('teacher','laoxu')

r.mset({'course':98,'age':20})

print(r.mget('teacher','course','age'))