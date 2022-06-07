from django.urls import path
from .views import *

urlpatterns = [
    path('', indexClassView.as_view(), name='index'),
]
