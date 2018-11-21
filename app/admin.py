from django.contrib import admin
from .models import KakaoService, WebGuideRequests, WebGuideReplies

# Register your models here.
admin.site.register(KakaoService)
admin.site.register(WebGuideRequests)
admin.site.register(WebGuideReplies)
