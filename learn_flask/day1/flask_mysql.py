
import pymysql

'''导入flask'''
from flask import Flask

app = Flask(__name__)

'''导入flask链接mysql数据库模块'''
from flask_sqlalchemy import  SQLAlchemy

# 创建的时候一定要加上pymysql
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:123456@127.0.0.1/country'

# 创建数据库实例对象，相当于自己写的db=。。。。。
db = SQLAlchemy(app)

@app.route('/api/hello')
def hello():
    from sqlalchemy import text
    sql = text('select * from sanguo;')
    result = db.engine.execute(sql)
    for row in result:
        app.logger.info(row)
    return 'hello world'

if __name__ == '__main__':

    app.run(host='0.0.0.0',debug = True)
