from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def shopperView(request):
    return HttpResponse('hello world')


def loginView(request):
    return HttpResponse('hello world')


def logoutView(request):
    return HttpResponse('hello world')


def shopcartView(request):
    return HttpResponse('hello world')
