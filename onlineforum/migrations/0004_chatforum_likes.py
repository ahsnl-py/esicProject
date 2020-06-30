# Generated by Django 3.0 on 2020-06-30 16:53

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('onlineforum', '0003_auto_20200630_1648'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatforum',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='forum_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
