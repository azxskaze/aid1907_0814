import redis
import random
r = redis.Redis(host='176.234.6.27',port='6379',db=0,password='123456')
# 模拟四个用户，两个活跃两个不活跃
r.setbit('user1:001',0,1)
r.setbit('user1:001',29,1)
r.setbit('user1:002',99,1)
for i in range(365):
    r.setbit('user1:003',i,random.randint(1,2)%2)
for i in range(365):
    r.setbit('user1:004',i,random.randint(1,2)%2)


user_list = r.keys('user1:*')
list_h=[]
list_c=[]
for i in user_list:
    count = r.bitcount(i)
    if count>150:
        list_h.append((i,count))
    else:
        list_c.append((i,count))
print('活跃用户：',list_h,'非活跃用户：',list_c)