# MidnightGoHome/app_fb/urls.py
from django.urls import path, re_path
from .views import *

urlpatterns = [
    re_path(r'^findpath$', kakaoi_findpath)
]
