from django.conf.urls import url

from user import views

urlpatterns=[
    url(r'^register', views.register),
    url(r'^lll',views.logon),
    url(r'^get_user_server', views.get_user_server),

]