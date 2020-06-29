
from django.conf import settings

from django.db import models

User = settings.AUTH_USER_MODEL

# Create your models here.
class Forum(models.Model):
    # id = models.AuthoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE) #many user can post in forum
    content = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to='images/', blank=True, null=True)

    class Meta:
        ordering = ['-id']
