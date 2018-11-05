#coding:utf-8
from django.conf.urls import url
from . import views

from django.conf import settings
from django.contrib.auth import views as auth_views  #django内置的
urlpatterns = [
    #url(r'^login/$',views.user_login,name="user_login"),#自定义的登录
    url(r'^login/$',auth_views.login,name="user_login"),#django内置的登录
    url(r'^logout/$',auth_views.logout,{"template_name":"account/logout.html"},name="user_logout"),#django内置的退出
    url(r'^register/$',views.register,name="user_register"),
]






