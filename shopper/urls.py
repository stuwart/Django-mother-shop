from django.urls import path
from .views import *

urlpatterns = [
    # path('.html', shopperView, name='shopper'),
    # path('/login.<int:id>.html', loginView, name='login'),
    # path('/logout.<int:id>.html', logoutView, name='logout'),
    # path('/shopcart.<int:id>.html', shopcartView, name='shopcart'),

    path('.html', shopperView, name='shopper'),
    path('/login.html', loginView, name='login'),
    path('/logout.html', logoutView, name='logout'),
    path('/shopcart.html', shopcartView, name='shopcart'),
]