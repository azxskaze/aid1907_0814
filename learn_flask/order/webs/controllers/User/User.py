from flask import Blueprint,render_template
route_user = Blueprint('user_page',__name__)

@route_user.route('/login')
def login():
    # 调用render_template模块可以直接返回指定html文件
    return render_template('user/login.html')
@route_user.route('/edit')
def edit():
    # 调用render_template模块可以直接返回指定html文件
    return render_template('user/edit.html')
@route_user.route('/rest-pwd')
def restPwd():
    # 调用render_template模块可以直接返回指定html文件
    return render_template('user/rest-pwd.html')