'''读数据库
    pymysql 读操作select
    游标具有可迭代性
'''
import pymysql

# 连接数据库
db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     password='123456',
                     database='books',
                     charset='utf8')

# 获取游标
cur = db.cursor()

# 获取数据
sql = "select id,title from book;"
a=cur.execute(sql)

# # 可以直接遍历游标
# for i in cur:
#     print(i)

# 获取所有查询结果
# 通过cur.fetchall()方法
# all_row = cur.fetchall()
# print(all_row)

# 获取查询的多个查询结果cur.fetchmany(2) 参数为想要获取的个数
# many_row = cur.fetchmany(2)
# print(many_row)

# 获取一个查询结果
one_row = cur.fetchone()
print(one_row)

cur.close()
db.close()