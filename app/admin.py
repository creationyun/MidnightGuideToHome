from django.contrib import admin
from .models import WebGuideRequests, WebGuideReplies, WebPubTransRoutesComparisons, WebBusTimetable

# Register your models here.
admin.site.register(WebGuideRequests)
admin.site.register(WebGuideReplies)
admin.site.register(WebPubTransRoutesComparisons)
admin.site.register(WebBusTimetable)
