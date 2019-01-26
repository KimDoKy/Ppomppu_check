from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    name = models. CharField(blank=True, max_length=200)

    def __str__(self):
        return f'{self.email}'
