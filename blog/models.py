#coding:utf-8
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class BlogArticles(models.Model):
	title = models.CharField(max_length=300)
#related_name作用是允许User反向查询到BlogArticles
	author = models.ForeignKey(User, related_name='blog_posts')
	body = models.TextField()
	publish = models.DateTimeField(default=timezone.now)

#规定了BlogArticles实例对象的显示顺序
	class Meta:
		ordering = ("-publish",)

	def __str__(self):
		return self.title

