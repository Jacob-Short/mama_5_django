# Generated by Django 3.2.8 on 2021-10-31 03:44

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user_post', '0002_userpost_picture'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReviewNotification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_created', models.DateTimeField(default=datetime.datetime(2021, 10, 31, 3, 44, 6, 782257, tzinfo=utc))),
                ('isNew', models.BooleanField(default=True)),
                ('review', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='review_noti', to='user_post.userpost')),
                ('user_created', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_created_review', to=settings.AUTH_USER_MODEL)),
                ('user_notified', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_notified_review', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]