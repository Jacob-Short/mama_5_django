from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils.translation import ugettext_lazy as _
from datetime import date


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, is_staff=False, is_admin=False):
        if not email:
            raise ValueError("Users must have an email")
        if not password:
            raise ValueError("Users must have a password")
        new_user = self.model(email=self.normalize_email(email))
        new_user.set_password(password)
        new_user.staff = is_staff
        new_user.admin = is_admin
        new_user.save(using=self._db)
        return new_user

    def create_staffuser(self, email, password=None):
        new_user = self.create_user(
            email,
            password=password,
            is_staff=True,
        )
        return new_user

    def create_superuser(self, email, password=None):
        new_user = self.create_user(
            email,
            password=password,
            is_staff=True,
            is_admin=True,
        )
        return new_user


class UserAccount(AbstractBaseUser):
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
    is_new = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=True)
    admin = models.BooleanField(default=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def is_active(self):
        return self.active

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin
