from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE
from django.utils import timezone


class MyUser(AbstractUser):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
