'''操作set'''
import pymysql
import redis

db = pymysql.connect(host='127.0.0.1',
                     user='root',
                     password='123456',
                     database='userdb',
                     charset='utf8')

cur = db.cursor()

r = redis.Redis(host='176.234.6.27', port='6379', db=0, password='123456')

r.sadd('set1',1,2,3)
r.sadd('set2',2,3,4)
# str1 = set()
# for i in r.smembers('set1'):
#     str1.add(i.decode())

str2 = b' '.join(r.smembers('set1'))
str3 = set(str2.decode().split(' '))
print(str3)

# 交集
r.sinterstore('new_set','set1','set2')
print(r.smembers('new_set'))
print(type(r.sinter('set1','set2')))

# 并集
r.sunionstore('new_b_set','set1','set2')
print(r.smembers('new_b_set'))

# 差集
r.sdiffstore('new_d_set','set1','set2')
print(r.smembers('new_d_set'))

cur.close()
db.close()