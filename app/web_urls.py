# MidnightGoHome/app/web_urls.py
from django.urls import path
from .views import web_index, web_guide_request, web_request_view

urlpatterns = [
    path('', web_index),
    path('guide_request/', web_guide_request),
    path('request_view/', web_request_view),
]
