from django.conf.urls import url
from note import views

urlpatterns = [
    url(r'^$', views.list_view),

    url(r'add$', views.add_view),
    url(r'del/(\d+)', views.del_view),
    url(r'show_note/(\d+)', views.show_view),
    url(r'update_note/(\d+)', views.update_view),

]