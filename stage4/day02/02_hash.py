'''pycharm操作哈希类型数据'''
import redis

r = redis.Redis(host='176.234.6.27', port='6379', db=0, password='123456')
user_dict = {
    'name':'saber',
    'attack':'Excalibur',
    'master':'Aimrashilo'
}
r.hmset('user002',user_dict)
user_dic = r.hgetall('user002')
print(user_dic)
user_list = r.hkeys('user002')
print(user_list)
r.hdel('user002','master')