from django.db import models
from user_account.models import User
from django.db.models.deletion import CASCADE
from user_message.models import Message
from django.utils import timezone

class MessageNotification(models.Model):
    message = models.ForeignKey(Message, on_delete=CASCADE, null=True, related_name='message_noti')
    user_created = models.ForeignKey(User, on_delete=CASCADE, null=True, related_name='user_created_message')
    user_notified = models.ForeignKey(User, on_delete=CASCADE, null=True, related_name='user_notified_message')
    time_created = models.DateTimeField(default=timezone.now())
    isNew = models.BooleanField(default=True)

    def __str__(self):
        return self.message