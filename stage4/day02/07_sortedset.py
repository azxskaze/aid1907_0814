'''操作有序列表'''
import redis

r = redis.Redis(host='176.234.6.27',
                port='6379',
                db=0,
                password='123456')
r.zadd('fruit:set',{'apple':10,'peach':5,'orange':6,'mongo':8})

# 查看所有
fruit_list = r.zrange('fruit:set',0,-1,withscores=True)
print(fruit_list,type(fruit_list))

# 范围查询
fruit_list1=r.zrangebyscore('fruit:set',6,12,start=0,num=2,withscores=True)
print(fruit_list1)

# 删除成员
r.zrem('fruit:set','apple')
print(r.zrange('fruit:set',0,-1))

# 增加分数
r.zincrby('fruit:set',3,'peach')
print(r.zscore('fruit:set','peach'))

r.zadd('fruit:set2',{'banana':3,'mongo':15,'cherry':20})

# 并集
r.zunionstore('fruit:set3',('fruit:set','fruit:set2'),aggregate='max')
print(r.zrange('fruit:set3',0,-1))


# 交集
r.zinterstore('fruit:set4',('fruit:set','fruit:set2'),aggregate='max')
print(r.zrange('fruit:set4',0,-1))
