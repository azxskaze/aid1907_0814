import pymysql
import redis
# 连接数据库
db = pymysql.connect(host='127.0.0.1',
                     user='root',
                     password='123456',
                     database='userdb',
                     charset='utf8')
# 创建游标对象
cur = db.cursor()

r = redis.Redis(host='176.234.6.27', port='6379', db=0, password='123456')

# 1,先到redis中查询
# 2,redis中没有，到mysql中查询，缓存到redis(设置过期时间)
username = input('请输入要查询的用户名：')
# 1,redis查
user_dic = r.hgetall(username)
if user_dic:
    print(user_dic)
else:
    sql = 'select * from user where name=%s'
    cur.execute(sql,username)
    user = cur.fetchone()
    print(user)
    if user:
        r.hmset(user[0],{'username':user[0],'age':user[1],'score':user[2]})
        r.expire(user[0],13)
    else:
        # 如果没查到就全部设置为null
        r.hmset(username, {'username': 'no', 'age': 'no', 'score': 'no'})
        r.expire(username, 13)

cur.close()
db.close()