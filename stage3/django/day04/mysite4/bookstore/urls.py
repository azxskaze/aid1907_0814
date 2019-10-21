from django.conf.urls import url

from bookstore import views

urlpatterns = [
    url(r'^add_book',views.add_book),
    url(r'^all_book', views.all_book),
    url(r'^detail/(\d+)', views.detail),
    url(r'^updatebook/(\d+)', views.update_book),
    url(r'^delete/(\d+)', views.delete)

]