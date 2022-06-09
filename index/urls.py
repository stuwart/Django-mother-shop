from django.urls import path
from .views import *

urlpatterns = [
    # path('', indexView, name='index'),
    path('', indexClassView.as_view(), name='index'),
]
