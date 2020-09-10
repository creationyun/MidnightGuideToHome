# MidnightGoHome/app/web_urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('', web_index),
    path('guide_request/', web_guide_request),
    path('request_view/<slug:condition>/', web_request_view),
    path('request_view/detail/<int:req_id>/', web_request_detail),
]
