#coding:utf-8
from django.conf.urls import url,include
from . import views

#urlpatterns老是容易搞错
urlpatterns = [
#views.blog_title声明了相应这个请求的函数
    url(r'^$',views.blog_title,name="blog_title"),
    url(r'(?P<article_id>\d)/$',views.blog_article,name="blog_article"),
    #url(r'^blog/(?P<article_id>\d)/$',views.blog_article,name="blog_article"),
]

