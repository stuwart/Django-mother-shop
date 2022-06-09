from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def commodityView(request):
    return HttpResponse('Hello world')


def detailView(request, id):
    return HttpResponse('Hello world')
