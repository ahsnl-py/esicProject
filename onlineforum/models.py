# Create your models here.
from django.db import models


# Create your models here.
class ChatForum(models.Model):
    # id = models.AuthoField(primary_key=True)
    content = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to='images/', blank=True, null=True)

    class Meta:
        ordering = ['-id']
