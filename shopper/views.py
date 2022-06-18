from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from .form import *
from .models import *
from django.contrib.auth.decorators import login_required
from commodity.models import *


@login_required(login_url='shopper/login.html')
def shopperView(request):
    title = '个人中心'
    classContent = 'informations'
    p = request.GET.get('p', 1)

    t = request.GET.get('t', '')

    payTime = request.session.get('payTime', '')
    if t and payTime and t == payTime:
        payInfo = request.session.get('payInfo', '')
        OrderInfos.objects.create(**payInfo)
        del request.session['payTime']
        del request.session['payInfo']

    orderInfos = OrderInfos.objects.filter(user_id=request.user.id).order_by('-created')
    paginator = Paginator(orderInfos, 7)
    try:
        pages = paginator.page(p)
    except PageNotAnInteger:
        pages = paginator.page(1)
    except EmptyPage:
        pages = paginator.page(paginator.num_pages)
    return render(request, 'shopper.html', locals())


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
        return render(request, 'login.html', locals())


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
    # 使用内置函数logout退出用户登录状态
    # logout(request)
    # 网页自动跳转到首页
    return redirect(reverse('index:index'))

def shopcartView(request):
    title = '我的购物车'
    classContent = 'shopcarts'
    id = request.GET.get('id', '')
    quantity = request.GET.get('quantity', '1')
    userID = request.user.id

    if id:
        CartInfos.objects.update_or_create(commodityInfos_id=id, user_id=userID, quantity=quantity)
        return redirect('shopper:shopcart')
    getUserID = CartInfos.objects.filter(user_id=userID)

    commodityDcit = {x.commodityInfos_id: x.quantity for x in getUserID}

    commodityInfos = CommodityInfos.objects.filter(id__in=commodityDcit.keys())
    return render(request, 'shopcart.html', locals())


def deleteAPI(request):
    return