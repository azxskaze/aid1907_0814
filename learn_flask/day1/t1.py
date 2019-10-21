from flask import Flask
from imooc import route_imooc
app = Flask(__name__)
app.register_blueprint(route_imooc,url_prefix='/this')

@app.route('/a')
def a():
    return 'aaaaaaaaaaaaaaa'
if __name__ == '__main__':
    app.run('176.234.6.35',debug=True)