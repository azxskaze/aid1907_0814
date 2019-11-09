import redis
import pymysql

class Update:
    def __init__(self):
        self.r = redis.Redis(host='176.234.6.27',port='6379',db=0,password='123456')
        self.db = pymysql.connect(host='127.0.0.1',
                     user='root',
                     password='123456',
                     database='userdb',
                     charset='utf8')
        self.cur = self.db.cursor()
    def update_mysql(self,score,name):
        upd = 'update user set score=%s where name=%s'

        try:
            self.cur.execute(upd,[score,name])
            self.db.commit()
            return True
        except Exception as e:
            print(e)
            self.db.rollback()

    def update_redis(self,score,name):
        self.r.hmset(name,{'score':score})
        self.r.expire(name,30)

    def run(self):
        name = input('plz key name')
        score = float(input('plz key score'))
        if self.update_mysql(score,name):
            self.update_redis(score,name)
if __name__ == '__main__':
    upd = Update()
    upd.run()
