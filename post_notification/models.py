from django.db import models
from user_account.models import User
from django.db.models.deletion import CASCADE
from user_post.models import UserPost
from django.utils import timezone

class ReviewNotification(models.Model):
    review = models.ForeignKey(UserPost, on_delete=CASCADE, null=True, related_name='review_noti')
    user_created = models.ForeignKey(User, on_delete=CASCADE, null=True, related_name='user_created_review')
    user_notified = models.ForeignKey(User, on_delete=CASCADE, null=True, related_name='user_notified_review')
    time_created = models.DateTimeField(default=timezone.now())
    isNew = models.BooleanField(default=True)

    def __str__(self):
        return self.review