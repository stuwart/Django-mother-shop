from django.contrib import admin
from .models import *


# Register your models here.

@admin.register(CartInfos)
class CartInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'quantity']


@admin.register(OrderInfos)
class OrderInfosAdmin(admin.ModelAdmin):
    list_display = ['id', 'price', 'created', 'state']
    list_filter = ['state']
    date_hierarchy = 'created'
