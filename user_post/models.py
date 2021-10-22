from django.db import models
from django.db.models.fields import DateField
from django.utils import timezone
from user_account.models import UserAccount


class UserPost(models.Model):

    CHOICES = [(1, 'True'), (2, 'False')]
    title = models.CharField(max_length=150)
    post = models.TextField()
    user_created = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name='created_by')
    time_created = DateField(default=timezone.now)
    isNew = models.BooleanField(choices=CHOICES, default=1)


    def __str__(self):
        return self.title