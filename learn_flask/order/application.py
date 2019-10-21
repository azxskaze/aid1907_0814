from flask import Flask
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
import os




class Application(Flask):
    def __init__(self,import_name,template_folder=None,root_path=None):
        super().__init__(import_name,template_folder=template_folder,root_path=root_path,static_folder=None)
        self.config.from_pyfile('config/base_setting.py')
        if 'ops_config' in os.environ:
            self.config.from_pyfile('config/%s_setting.py'%os.environ['ops_config'])


        db.init_app(self)
db = SQLAlchemy()
# 将静态网页文件路径修改为当前路径下webs路径下的template里面
app = Application(__name__,template_folder=os.getcwd()+'/webs/templates',root_path=os.getcwd())
manager = Manager(app)


from common.libs.UrlManager import UrlManager
'''函数模板'''
app.add_template_global(UrlManager.buildStaticUrl,'buildStaticUrl')
app.add_template_global(UrlManager.buildUrl,'buildUrl')

