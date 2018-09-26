# MidnightGoHome/app/web_urls.py
from django.urls import path
from .views import web_index, web_guide_request

urlpatterns = [
    path('', web_index),
    path('guide_request/', web_guide_request),
]
