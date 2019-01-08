# MidnightGoHome/app_fb/urls.py
from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('findpath/', kakaoi_findpath)
]
