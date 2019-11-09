import redis

r = redis.Redis(host='176.234.6.27',port=6379,db=0,password='123456')

r.rpush('tedu:teachers','qtx','lxv','gxn','wwc')
# r.lrem('tedu:teachers',0,'qtx')
# r.lrem('tedu:teachers',0,'lxv')
# r.lrem('tedu:teachers',0,'gxn')
# r.lrem('tedu:teachers',0,'wwc')

r.linsert('tedu:teachers','after','lxz','txh')
r.ltrim('tedu:teachers',0,3)
# while True:
#     l = r.brpop('tedu:teachers',3)
#     #l: (b'tedu:teachers', b'lxv')
#     if l:
#         print(l)
#     else:
#         break

a = r.lrange('tedu:teachers',0,5)
print(a)