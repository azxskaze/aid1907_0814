from django.conf.urls import url

from index import views

urlpatterns=[
    url(r'^index/',views.index),
    url(r'^is_login/', views.is_login),
    url(r'^show/', views.show)

]