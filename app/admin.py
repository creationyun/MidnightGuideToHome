from django.contrib import admin
from .models import WebGuideRequests, WebGuideReplies, WebPubTransRoutesComparisons

# Register your models here.
admin.site.register(WebGuideRequests)
admin.site.register(WebGuideReplies)
admin.site.register(WebPubTransRoutesComparisons)
