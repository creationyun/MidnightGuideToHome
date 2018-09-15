from django.db import models

# Create your models here.
class KakaoService(models.Model):
    user = models.CharField(max_length=100, primary_key=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    dhcp_status = models.BooleanField(default=False)
    nightbus_status = models.BooleanField(default=False)
    paidtoilet_status = models.BooleanField(default=False)
