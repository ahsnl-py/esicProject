# Create your models here.
import random 
from django.conf import settings 
from django.db import models

User = settings.AUTH_USER_MODEL

class ChatForumLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    forum = models.ForeignKey("ChatForum", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    

# Create your models here.
class ChatForum(models.Model):
    # id = models.AuthoField(primary_key=True)
    parent = models.ForeignKey("self", null=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chatforums') 
    content = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to='images/', blank=True, null=True)
    likes = models.ManyToManyField(User, related_name="forum_user", blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-id']

    @property
    def is_repost(self):
        return self.parent != None 