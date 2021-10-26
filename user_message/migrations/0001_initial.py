# Generated by Django 3.2.8 on 2021-10-25 22:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(max_length=500)),
                ('time_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('isNew', models.BooleanField(choices=[(1, 'True'), (2, 'False')], default=1)),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='message_author', to=settings.AUTH_USER_MODEL)),
                ('recipient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='message_recipient', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
