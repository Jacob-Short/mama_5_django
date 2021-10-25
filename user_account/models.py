from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from datetime import date


class UserAccount(AbstractUser):
    """a user account for site"""

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
    username = models.CharField(max_length=50, blank=True, null=True, unique=True)
    email = models.EmailField(_("email address"), unique=True)
    picture = models.ImageField(
        upload_to="images/", max_length=100, default="images/download.png"
    )
    bio = models.TextField(null=True, blank=True)
    isNew = models.BooleanField(default=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name", "last_name"]

    class Meta:
        verbose_name = _('useraccount')
        verbose_name_plural = _('useraccounts')

    def __str__(self):
        return self.email
