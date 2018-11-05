#coding:utf-8
#与表单有关的类

from django import forms
from django.contrib.auth.models import User    #引用Uer模型
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class RegistrationForm(forms.ModelForm):      #继承前面的forms.ModelForm类
    password = forms.CharField(label="Password",widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm Password",widget=forms.PasswordInput)

    class Meta:         #声明表单类所用的数据模型
        model = User
        fields = ("username","email")   #表明选用的数据库字段

    def clean_password2(self):          #比较密码前后是否一致
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("passwords do not match.")
        return cd['password2']


