# Generated by Django 3.0 on 2020-07-04 16:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('onlineforum', '0005_chatforum_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatforum',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chatforums', to=settings.AUTH_USER_MODEL),
        ),
    ]