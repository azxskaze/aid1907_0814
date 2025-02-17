'''此文件夹存放蓝图'''

from application import app
from webs.controllers.index import route_index
from webs.controllers.User.User import route_user
from webs.controllers.static import route_static
from webs.controllers.account.Account import route_account
from webs.controllers.finance.Finance import route_finance
from webs.controllers.food.Food import route_food
from webs.controllers.member.Member import route_member
from webs.controllers.stat.Stat import route_stat





app.register_blueprint(route_index,url_prefix = '/')
app.register_blueprint(route_user,url_prefix = '/user')
app.register_blueprint(route_static,url_prefix = '/static')
app.register_blueprint(route_account,url_prefix = '/account')
app.register_blueprint(route_finance,url_prefix = '/finance')
app.register_blueprint(route_food,url_prefix = '/food')
app.register_blueprint(route_member,url_prefix = '/member')
app.register_blueprint(route_stat,url_prefix = '/stat')








