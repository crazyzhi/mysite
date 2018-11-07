#coding:utf-8
from django.contrib import admin
from .models import UserProfile
#admin.py的主要作用是将某些内容注册到后端管理界面
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("user","birth","phone")     #列出列表中的项目
    list_filter = ("phone",)                    #规定网页右边filter中显示的内容

admin.site.register(UserProfile,UserProfileAdmin)





# Register your models here.
