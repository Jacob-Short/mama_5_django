# Generated by Django 3.2.8 on 2021-10-31 03:51

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('message_notification', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messagenotification',
            name='time_created',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 31, 3, 51, 5, 144297, tzinfo=utc)),
        ),
    ]