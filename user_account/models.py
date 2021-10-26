from django.apps import apps
from django.db import models
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



class User(AbstractUser):
    """a user account for site"""

    username = models.CharField(
        max_length=150,
    )

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



    email = models.EmailField(_("email address"), unique=True, blank=False)
    picture = models.ImageField(
        upload_to="images/",
        max_length=100,
        default="images/default_profile_picture.jpeg",
    )
    bio = models.TextField(_("bio"), null=True, blank=True)

    is_new = models.BooleanField(
        _("new status"),
        default=False,
    )


    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = []


    def __str__(self):
        return self.email

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
