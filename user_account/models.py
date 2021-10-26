from django.apps import apps
from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.core.validators import EmailValidator
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.hashers import make_password
from django.contrib import auth
from datetime import date


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password=None, **other_fields):
        if not email:
            raise ValueError("Users must have an email")
        if not password:
            raise ValueError("Users must have a password")

        new_user = self.model(email=self.normalize_email(email), **other_fields)
        new_user.password = make_password(password)
        new_user.save(using=self._db)
        return new_user

    def create_user(self, email, password=None, **other_fields):
        other_fields.setdefault("is_staff", False)
        other_fields.setdefault("is_admin", False)
        other_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **other_fields)

    def create_superuser(self, email, password=None, **other_fields):
        other_fields.setdefault("is_staff", True)
        other_fields.setdefault("is_superuser", True)
        other_fields.setdefault("is_admin", True)

        if other_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if other_fields.get("is_admin") is not True:
            raise ValueError("Superuser must have is_admin=True.")
        if other_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **other_fields)


class User(AbstractBaseUser, PermissionsMixin):
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

    username_validator = EmailValidator()

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

    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
    )

    is_admin = models.BooleanField(
        _("admin status"),
        default=False,
    )

    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
