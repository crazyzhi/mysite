#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate,login   #django内置的用户认证和管理应用的方法
from .forms import LoginForm,RegistrationForm

def user_login(request):
    if request.method == "POST":        #request.method返回HTTP请求的字符串
        login_form = LoginForm(request.POST)#request.POST，GET方法多用于查询，POST方法多用于数据写入和更新
        if login_form.is_valid():       #验证输入的数据是否合法
            cd = login_form.cleaned_data
            user = authenticate(username=cd['username'],password=cd['password'])#验证传入的数据是否合法

            if user:
                login(request,user)#利用得到的参数实现登录
                return HttpResponse("Welcome You. You have been authenticated successfully")
            else:
                return HttpResponse("Invalid login")
    if request.method == "GET":
        login_form = LoginForm()
        return render(request,"account/login.html",{"form":login_form})

def register(request):
    if request.method == "POST":
        user_form = RegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)     #结果生成了一个数据对象
            new_user.set_password(user_form.cleaned_data['password'])   #设置了对象的密码（经校验过的）
            new_user.save()     #保存到数据库中
            return HttpResponse("successfully")
        else:
            return HttpResponse("sorry, your can not register.")
    else:
        user_form = RegistrationForm()
        return render(request,'account/register.html',{"form":user_form})





# Create your views here.
