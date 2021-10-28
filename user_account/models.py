from django.apps import apps
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import (
    AbstractUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.core.validators import EmailValidator
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.hashers import make_password
from django.contrib import auth
from datetime import date

from django.db.models.signals import post_save
from django.dispatch import receiver


class User(AbstractUser):
    """a user account for site"""

    def __str__(self):
        return self.username




class Profile(models.Model):
    '''OTO with user for personal attributes'''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(
        max_length=150,
        blank=True,
        null=True,
    )
    last_name = models.CharField(
        max_length=150,
        blank=True,
        null=True,
    )
    email = models.EmailField()
    bio = models.TextField(_("bio"), null=True, blank=True)
    profile_picture = models.ImageField(
        upload_to="images/",
        max_length=100,
        default="images/default_profile_picture.jpeg",
    )
    is_new = models.BooleanField(
        _("new status"),
        default=False,
    )
    created_at = models.DateTimeField(default=timezone.now())

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

