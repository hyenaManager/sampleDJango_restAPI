from django.urls import path
from .views import *

urlpatterns = [
    path('get/', getData),
    path('create/',createData)
]