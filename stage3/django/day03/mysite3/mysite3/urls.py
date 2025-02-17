from . import views
"""day02homework URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin


# 当前文件路径为：mysite3/urls.py 主路由
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index$', views.index),
    url(r'^shebao', views.shebao),
    # 127.0.0.1：8000/test_url
    url(r'^test_url', views.test_url),
    url(r'^page$', views.page_view,name='pp'),
    # 127.0.0.1：8000/page1~xxxx
    url(r'^page(\d+)', views.pagen_view, name='pn'),
    # 127.0.0.1：8000/test_static
    url(r'^test_static', views.test_static),

    # 127.0.0.1:8000/sports/xxx
    url(r'^sports/', include('sports.urls')),
    url(r'^news/', include('news.urls')),
    url(r'^music/', include('music.urls')),
    url(r'^index/', include('index.urls')),

]
