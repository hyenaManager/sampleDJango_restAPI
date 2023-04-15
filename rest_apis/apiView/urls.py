from django.urls import path
from .views import *

urlpatterns = [
    path('basic/', BookView.as_view()),
]