'''通过蓝牙方法进行统一路由规划'''

from flask import Blueprint,Flask
route_imooc = Blueprint('imooc_page',__name__)

app = Flask(__name__)
app.register_blueprint(route_imooc,url_prefix ='/imooc')

@route_imooc.route('/')
def index():
    return 'imooc_page'

@route_imooc.route('/hello')
def hello():
    return 'imooc_helloworlrd'

if __name__ == '__main__':
    app.run()