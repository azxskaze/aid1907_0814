import pymysql
import time
# 连接数据库
db = pymysql.connect(host = 'localhost',
                     port = 3306,
                     user = 'root',
                     password = '123456',
                     database = 'db2',
                     charset = 'utf8')

cur = db.cursor()

try:
    sql1 = 'insert into bank values("ccc",10212)'
    sql2 = 'insert into bank values("ddd"1,10212)'
    cur.execute(sql1)
    cur.execute(sql2)
    db.commit()
except:
    db.rollback()

cur.close()
db.close()