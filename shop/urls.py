
from django.contrib import admin
from django.urls import path,re_path,include
from django.views.static import serve
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('index.urls', 'index'), namespace = 'index')),
    path('commodity', include(('commodity.urls', 'commodity'), namespace = 'commodity')),
    path('shopper', include(('shopper.urls', 'shopper'), namespace = 'shopper')),

    # 配置媒体文件夹的路由信息
    re_path('media/(?P<path>.*)', serve, { 'document_root':settings.MEDIA_ROOT}, name = 'media'),
]

