from django.db import models
from django.contrib.auth.models import AbstractUser



class UserAccount(AbstractUser):
    '''a user account for site'''

    CHOICES = [(1, 'True'), (2, 'False')]
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    picture = models.ImageField(upload_to='images/', max_length=100, default='images/download.png')
    bio = models.TextField(null=True, blank=True)
    isNew = models.BooleanField(choices=CHOICES, default=1)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.first_name + self.last_name
