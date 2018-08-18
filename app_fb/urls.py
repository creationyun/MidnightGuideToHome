# MidnightGoHome/app_fb/urls.py
from django.urls import include, re_path
from .views import BotView

urlpatterns = [
    re_path(r'^09b8713ddc62d7e8331e45f11918a05cedeec90a3e34467ff8/?$', BotView.as_view())
]
