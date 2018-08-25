from django.db import models
from django.utils import timezone

# Create your models here.
class KakaoDHCPService(models.Model):
    user = models.CharField(max_length=100)
    lastused_date = models.DateTimeField(
        default=timezone.now, auto_now=True, auto_now_add=True
    )
    status = models.BooleanField(default=False)
