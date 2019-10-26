from django.conf.urls import url
from . import views
urlpatterns=[
    url(r'^email',views.email),
    url(r'^send1', views.send),
    url(r'^send_to', views.sendto),

]