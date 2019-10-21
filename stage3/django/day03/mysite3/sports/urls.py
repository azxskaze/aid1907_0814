'''这个文件需要自己手动创建
路由匹配规则自己写'''
from django.conf.urls import url
from .import views
urlpatterns = [
    # http://127.0.0.1:8000/sports/index
    # 这个时候主路由已经匹配走了，不需要再匹配了
    url(r'^index$',views.index)



]