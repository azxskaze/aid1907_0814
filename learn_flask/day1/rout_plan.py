'''flask路由规划

版本管理 每次发版都有个版本号：20190911400
                            20190912500
'''
import pymysql

'''导入flask'''
from flask import Flask,url_for

'''导入自定义蓝图导航模块（其他程序）'''
from imooc import route_imooc

'''导入自定义url和版本管理模块'''
from libs.UrlManager import UrlManager


app = Flask(__name__)
app.register_blueprint(route_imooc,url_prefix ='/imooc')

'''导入flask链接mysql数据库模块'''
from flask_sqlalchemy import  SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:123456@127.0.0.1/country'
# 创建数据库实例对象，相当于自己写的db=。。。。。
db = SQLAlchemy(app)


@app.route('/')
def hello_world():

    # url_for()可以通过视图的方法名找到对应的链接
    # url---->'/api'

    url = url_for('.index')
    # 将链接管理和框架剥离开来
    url1 = UrlManager.buildUrl('/api')

    url2 = UrlManager.buildStaticUrl('/css/bootstrap.css')
    msg = 'Hello world,url:%s.url_1:%s url2:%s'%(url,url1,url2)
    app.logger.info(msg)
    app.logger.error(msg)


    return msg

    # return 'Hello world,url:%s.url_1:%s url2:%s'%(url,url1,url2)

@app.route('/api')
def index():
    return 'INDEX PAGE'

@app.route('/api/hello')
def hello():
    from sqlalchemy import text
    sql = text('select * from sanguo;')
    result = db.engine.execute(sql)
    for row in result:
        app.logger.info(row)
    return 'hello world'

@app.errorhandler(404)
def page_not_found(error):
    app.logger.error(error)
    return '页面出错',404

if __name__ == '__main__':

    app.run(host='0.0.0.0',debug = True)
