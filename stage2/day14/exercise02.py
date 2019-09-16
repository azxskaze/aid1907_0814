import pymysql

class Join:
    def __init__(self):
        self.db = pymysql.connect(host='localhost',
                             port=3306,
                             user='root',
                             password='123456',
                             database='dict1',
                             charset='utf8')
        self.cur = self.db.cursor()
    def login(self):
        user=input('用户名')
        password=input('密码')
        sql = "select usr from user where usr=%s;"
        self.cur.execute(sql,[user])
        data = self.cur.fetchone()
        if data:
            return False
        sql1 = "insert into user values (%s,%s);"
        try:
            self.cur.execute(sql1,[user,password])
            self.db.commit()
            return True
        except Exception as e:
            print(e)
            self.db.rollback()
    def logon(self):
        user = input('用户名')
        password = input('密码')
        sql = "select * from user where usr=%s and password=%s;"
        self.cur.execute(sql,[user,password])
        data = self.cur.fetchone()
        if data:
            return True
    def main(self):
        while True:
            key = input('plz')
            if key == '1':
                if self.login():
                    print('注册成功')
                else:
                    print('注册失败（用户名已存在）')
            elif key == '2':
                if self.logon():
                    print('（登陆成功）')
                else:
                    print('（登录失败（用户名/密码错误））')

if __name__ == '__main__':
    a = Join()
    a.main()

