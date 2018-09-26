"""MidnightGuideToHome URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import include, path, re_path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('web/', include('app.web_urls')),
    re_path(r'^keyboard$', views.keyboard),
    re_path(r'^message$', views.message),
    re_path(r'^friend/(?P<user_key>[\w-]+)$', views.friend_block),
    re_path(r'^friend$', views.friend_add),
    re_path(r'^chat_room/(?P<user_key>[\w-]+)$', views.friend_leave),
    re_path(r'^(?P<image_name>media/[\w-]+.*)$', views.image_load),
    path('fb_app/', include('app_fb.urls')),
]
