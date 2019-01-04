# MidnightGoHome/app_fb/urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('findpath/', kakaoi_findpath)
]
