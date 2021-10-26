from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
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
    email = models.EmailField(_("email address"), unique=True)
    picture = models.ImageField(
        upload_to="images/",
        max_length=100,
        default="images/default_profile_picture.jpeg",
    )
    bio = models.TextField(_("about"), null=True, blank=True)
    is_new = models.BooleanField(default=True)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=True)
    admin = models.BooleanField(default=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin
