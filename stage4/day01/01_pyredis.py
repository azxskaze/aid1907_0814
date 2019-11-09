'''
redis数据库的基本操作
'''
import redis


# 连接到数据库
r = redis.Redis(host='176.234.6.27',port=6379,db=0,password='123456')

# 直接操作数据库  kry_list :[b'',b'',b;'']
key_list = r.keys('*')

# 转换为普通的字符串
# for i in range(len(key_list)):
#     key_list[i] = key_list[i].decode()
# print(key_list)

# 查看key的类型
print(r.type('name'))

# 返回值0/1
print(r.exists('name'))

# 删除
# r.delete('age')

