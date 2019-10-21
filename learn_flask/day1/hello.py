from flask import Flask
from imooc import route_imooc
app = Flask(__name__)

@app.route('/111')
def hello_world():
    return 'hello world!'

if __name__ == '__main__':
    app.run()
