from django.urls import path
from .views import *

urlpatterns = [
    path('.html', shopperView, name='shopper'),
    path('/login.html', loginView, name='login'),
    path('/logout.html', logoutView, name='logout'),
    path('/shopcart.html', shopcartView, name='shopcart'),
]