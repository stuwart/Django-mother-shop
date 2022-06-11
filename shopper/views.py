from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from .form import *


# Create your views here.

def shopperView(request):
    return HttpResponse('hello world')

def loginView(request):
    title = '用户登录'
    classContent = 'logins'
    if request.method == 'POST':
        infos = LoginModelForm(data=request.POST)
        data = infos.data
        username = data['username']
        password = data['password']

        if User.objects.filter(username=username):
            user = authenticate(username=username, password=password)

            if user:
                login(request, user)
                return redirect(reverse('shopper:shopper'))
        else:
            state = '注册成功'
            d = dict(username=username, password=password, is_staff=1, is_active=1)
            user = User.objects.create_user(**d)
            user.save()

    else:
        infos = LoginModelForm()
        return render(request,'login.html',locals())


# def loginView(request):
#     title = '用户登录'
#     classContent = 'logins'
#     if request.method == 'POST':
#         infos = LoginForm(data=request.POST)
#         if infos.is_valid():
#             data = infos.cleaned_data
#             username = data['username']
#             password = data['password']
#
#             if User.objects.filter(username=username):
#                 user = authenticate(username=username, password=password)
#
#                 if user:
#                     login(request, user)
#                     return redirect(reverse('shopper:shopper'))
#             else:
#                 state = '注册成功'
#                 d = dict(username=username, password=password, is_staff=1, is_active=1)
#                 user = User.objects.create_user(**d)
#                 user.save()
#         else:
#             error_msg = infos.errors.as_json()
#             print(error_msg)
#     else:
#         infos = LoginForm()
#         return render(request,'login.html',locals())




def logoutView(request):
    return HttpResponse('hello world')


def shopcartView(request):
    return HttpResponse('hello world')
