from ipaddress import ip_address
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass


class WebAppMeta(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    hostname = models.CharField(max_length=20)
    engine = models.CharField(max_length=20)
    visitor_ip = models.GenericIPAddressField()
    