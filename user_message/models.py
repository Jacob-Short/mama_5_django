from django.db import models
from django.utils import timezone
from user_account.models import User


class Message(models.Model):

    CHOICES = [(1, "True"), (2, "False")]

    message = models.TextField(max_length=500)
    creator = models.ForeignKey(
        User, related_name="%(class)s_author", null=True, on_delete=models.CASCADE
    )
    recipient = models.ForeignKey(
        User, related_name="%(class)s_recipient", null=True, on_delete=models.CASCADE
    )
    time_created = models.DateTimeField(default=timezone.now)
    isNew = models.BooleanField(choices=CHOICES, default=1)

    def __str__(self):
        return self.message
