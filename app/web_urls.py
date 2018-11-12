# MidnightGoHome/app/web_urls.py
from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', web_index),
    path('guide_request/', web_guide_request),
    path('request_view/', web_request_view),
    path('request_view/<int:req_id>/', web_request_detail),
]
