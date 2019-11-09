from django.conf.urls import url
from . import views
urlpatterns=[
    url(r'^$',views.users),
    # 127.0.0.1:8000/v1/users/<username>
    url(r'^/(?P<username>\w{1,11})$', views.users),
    # 127.0.0.1;v1/users/<username/avatar>
    url(r'^/(?P<username>\w{1,11})/avatar$', views.users_avatar),

]