import pymysql
import re
db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     password='123456',
                     database='dict1',
                     charset='utf8')
cur = db.cursor()
f = open('dict.txt','r')

for line in f:

    # list1 = line.split(' ')
    # word = list1[0]
    # str1 = ' '.join(list1[1:len(list1)]).strip()
    sql = "insert into words (word,mean) values (%s,%s);"
    # cur.execute(sql,[word,str1])
    tup = re.findall(r'(\S+)\s+(.*)',line)[0]
    cur.execute(sql,tup)
try:
    db.commit()
except:
    db.rollback()
cur.close()
db.close()
f.close()






