from django.shortcuts import render
from commodity.models import *


# Create your views here.

def indexView(request):
    title = '首页'
    classContent = ' '
    commodityInfos = CommodityInfos.objects.order_by('-sold').all()[:8]

    types = Types.objects.all()
    cl = [x.seconds for x in types if x.firsts == '儿童服饰']
    clothes = CommodityInfos.objects.filter(types__in=cl).order_by('-sold')[:5]
    fl = [x.seconds for x in types if x.firsts == '奶粉辅食']
    food = CommodityInfos.objects.filter(types__in=fl).order_by('-sold')[:5]
    gl = [x.seconds for x in types if x.firsts == '儿童用品']
    goods = CommodityInfos.objects.filter(types__in=gl).order_by('-sold')[:5]
    return render(request, 'index.html', locals())
