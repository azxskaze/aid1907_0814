from django.conf.urls import url
from user import views

urlpatterns = [
    url(r'reg$', views.reg),
    url(r'login$', views.login_view),
    url(r'logout$', views.logout_view),

    url(r'index$', views.index),
    url(r'cs$', views.cs),

]