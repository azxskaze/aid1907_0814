from django.conf.urls import url
from index import views

urlpatterns = [
    url(r'set_cookies/', views.set_cookies),
    url(r'get_cookies/', views.get_cookies),
    url(r'get_session/', views.get_session),
    url(r'set_session/', views.set_session),
]