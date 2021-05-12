# MidnightGoHome/app/web_urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('', web_index, name='web_index'),
    path('guide_request/', web_guide_request, name='web_guide_request'),
    path('request_view/<slug:condition>/', web_request_view, name='web_request_view'),
    path('request_view/detail/<int:req_id>/', web_request_detail),
    path('pub_trans_routes_comparisons/', web_pub_trans_routes_comparisons, name='web_pub_trans_routes_comparisons')
]
