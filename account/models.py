#coding:utf-8
# #from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):    #建立userprofile的数据表
    user = models.OneToOneField(User,unique=True)   #声明user与userprofile是一对一的关系
    birth = models.DateField(blank=True,null=True)
    phone = models.CharField(max_length=20,null=True)

    def __str__(self):
        return 'user {}'.format(self.user.username)
class UserInfo(models.Model):
    user = models.OneToOneField(User,unique=True)
    school = models.CharField(max_length=100,blank=True)
    company = models.CharField(max_length=100,blank=True)
    profession = models.CharField(max_length=100,blank=True)
    address = models.CharField(max_length=100,blank=True)
    aboutme = models.TextField(blank=True)

    def __str__(self):
        return "user:{}".format(self.user.username)