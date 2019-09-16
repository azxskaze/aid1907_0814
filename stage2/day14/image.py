'''
save_file
二进制文件存取实例
'''
import pymysql

import pymysql
import re
db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     password='123456',
                     database='dict1',
                     charset='utf8')
cur = db.cursor()
with open('Xmind.jpg','rb') as f:
    data = f.read()
    sql = "insert into images values(1,%s,%s)"
    cur.execute(sql,[data,'sss'])
db.commit()
cur.close()
db.close()
f.close()






