from django.db import models
from django.contrib.auth.models import AbstractUser
from . import provider
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    provider = models.CharField(max_length=20, choices=provider.PROVIDER_CHOICES, default="app")
    access_key = models.CharField(max_length=255, blank=True)
    refresh_token = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f'{self.email}'
