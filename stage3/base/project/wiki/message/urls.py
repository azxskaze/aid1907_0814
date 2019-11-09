from django.conf.urls import url

from message import views

urlpatterns = [
    url(r'^(?P<topic_id>\w{1,11})$',views.message),
    url(r'^/(?P<topic_id>\d+)$',views.message),
]