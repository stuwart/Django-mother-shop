from django.shortcuts import render
from commodity.models import *
from django.views.generic.base import TemplateView


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


class indexClassView(TemplateView):
    template_name = 'index.html'  # 设置模板名，意思为网页内容由'index.html'生成
    template_engine = None  # 设置解析模板的模板引擎 ， None为默认
    content_type = None  # 设置相应内容的数据格式，None为使用text/html格式
    extra_context = {'title': '首页', 'classContent': ''}  # 设置的额外变量

    def get_context_data(self, **kwargs):  # 获取属性extra_content的值
        context = super().get_context_data(**kwargs)
        context['commodityInfos'] = CommodityInfos.objects.order_by('-sold').all()[:8]
        types = Types.objects.all()
        cl = [x.seconds for x in types if x.firsts == '儿童服饰']
        context['clothes'] = CommodityInfos.objects.filter(types__in=cl).order_by('-sold')[:5]
        fl = [x.seconds for x in types if x.firsts == '奶粉辅食']
        context['food'] = CommodityInfos.objects.filter(types__in=fl).order_by('-sold')[:5]
        gl = [x.seconds for x in types if x.firsts == '儿童用品']
        context['goods'] = CommodityInfos.objects.filter(types__in=gl).order_by('-sold')[:5]
        return context

    def get(self, request, *args, **kwargs):  # 定义GET请求处理方法
        pass
        context = self.get_context_data(**kwargs)  # get_context_data获取整个视图所有变量并赋值给context
        return self.render_to_response(context)  # 将context传递给render_··方法

    def post(self, request, *args, **kwargs):  # 与GET请求处理方法类似
        pass
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)
