from django.db import models

# Create your models here.
class KakaoDHCPService(models.Model):
    user = models.CharField(max_length=100)
    status = models.BooleanField(default=False)
