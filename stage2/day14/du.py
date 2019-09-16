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
with open('xmind.jpg','wb') as f:
    sql = "select image1 from images"
    cur.execute(sql)
    data=cur.fetchone()[0]
    f.write(data)

db.commit()
cur.close()
db.close()







