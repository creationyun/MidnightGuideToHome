from django.db import models

# Create your models here.
class KakaoDHCPService(models.Model):
    user = models.CharField(max_length=100)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)
