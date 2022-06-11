from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import *
from django.db.models import F


# Create your views here.
def commodityView(request):
    title = '商品列表'  ##对应base.html 的模板变量 title
    classContent = 'commoditys'
    # 根据Types生成分类列表
    firsts = Types.objects.values('firsts').distinct()  # 对Types模型去重查询， 获取商品一级分类
    typeList = Types.objects.all()  # 查询Types所有数据

    t = request.GET.get('t', '')  # 为整型。代表模型Types的主键ID
    s = request.GET.get('s', 'sold')  # 设置商品的排序方式，默认为sold
    p = request.GET.get('p', 1)  # 设置商品信息的页数，默认为1
    n = request.GET.get('n', '')  # 搜索功能的关键字，与CommodityInfos模型进行模糊匹配

    # 根据参数查询商品信息
    commodityInfos = CommodityInfos.objects.all()
    if t:
        types = Types.objects.filter(id=t).first()  # 查询某个分页的商品信息，
        commodityInfos = commodityInfos.filter(types=types.seconds)
    if s:
        commodityInfos = commodityInfos.order_by('-' + s)  # 设置商品的排序方式
    if n:
        commodityInfos = commodityInfos.filter(name__contains=n)  # 与name字段进行模糊匹配

    paginator = Paginator(commodityInfos, 6)
    try:
        pages = paginator.page(p)
    except PageNotAnInteger:
        pages = paginator.page(1)
    except EmptyPage:
        pages = paginator.page(paginator.num_pages)

    return render(request, 'commidity.html', locals())


def detailView(request, id):
    title = '商品介绍'
    classContent = 'details'
    commoditys = CommodityInfos.objects.filter(id=id).first()
    items = CommodityInfos.objects.exclude(id=id).order_by('-sold')[:5]  # 查询前五名销量最高的商品信息，exclude将当前商品信息排除
    likeList = request.session.get('likes', [])  # session会话
    likes = True if id in likeList else False  # 判断likeList是否含有当前商品的主键ID
    return render(request, 'details.html', locals())


def collectView(request):
    id = request.GET.get('id', '')  #
    result = {'result': '已收藏'}
    likes = request.session.get('likes', [])
    if id and not int(id) in likes:
        # 对商品的收藏数量自增+1
        CommodityInfos.objects.filter(id=id).update(likes=F('likes') + 1)
        result['result'] = '收藏成功'
        request.session['likes'] = likes + [int(id)]
    return JsonResponse(result)
