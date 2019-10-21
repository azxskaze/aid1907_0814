import pymysql
import time
# 连接数据库
db = pymysql.connect(host = 'localhost',
                     port = 3306,
                     user = 'root',
                     password = '123456',
                     database = 'country',
                     charset = 'utf8')
# 获取游标（游标：用来操作数据库，执行sql语句，得到执行结果）
cur = db.cursor()
# sql = "insert into student (name) values(%s)"
# for i in range(2000000):
#     print(i)
#     str1='name'+str(i)
#     cur.execute(sql,str1)
# db.commit()


# sql = "insert into student values(%s,%s)"
# list1 = [1,'name0']
# for i in range(2,2000000):
#     list1.append(i)
#     list1.append('name'+str(i))
#     sql+=',(%s,%s)'
# cur.execute(sql,list1)
# db.commit()

data_list = []
t1 = time.time()
for i in range(2000000):
    name = 'Tom%s'%(i)
    data_list.append(name)
t2 = time.time()
print('name is ready! cost %s second'%(t2-t1),t2-t1)
ins = 'insert into student' \
      ' (name) values(%s)'
cur.executemany(ins,data_list)
db.commit()
t3 = time.time()
print('***',t3-t2)