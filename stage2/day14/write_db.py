'''write_db
    pymysql写操作
    '''
import pymysql

db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     password='123456',
                     database='books',
                     charset='utf8')
cur = db.cursor()
# 执行语句
title = input('title')
price = int(input('price'))
level = input('level')
try:
    # 合成一个正确的sql语句才能正确的commit
    # sql = "insert into book values(13,'%s','s555a',%f,'1990-12-9','%s','sa')"%(title,price,level)
    # sql语句的值参量可以通过execute传入
    # sql = "insert into book values(11,%s,'s555a',%s,'1990-12-9',%s,'sa')"
    # cur.execute(sql,[title,price,level])
    # cur.execute(sql)

    # 修改
    # sql = "update book set title='aaaaaaa' where id=10"
    # cur.execute(sql)

    # # 删除
    # sql1 = "delete from book where id=11"
    # cur.execute(sql1)

    # 提交到数据库
    # 一次commit可以提交多次执行
    db.commit()

except Exception as e:
    print(e)
    db.rollback()
    #如果执行出错回滚到没有执行commit语句之前

# 关闭游标
cur.close()
# 关闭数据库
db.close()
