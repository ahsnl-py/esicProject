
from django.conf import settings
from django.db import models
from django.db.models.signals import post_save

User = settings.AUTH_USER_MODEL

class Profile(models.Model):
    PROGRAM_STATUS = (
        ('3rd year', 
        'Theoritical Fundamentals Of Mechanical Engineering'),
        ('4th year', 
        'Mechanical Engineering'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=50, choices=PROGRAM_STATUS, 
                              default='3rd year')

def user_did_save(sender, instance, created, *args, **kwargs):
    if created:
        Profile.objects.get_or_create(user=instance)

post_save.connect(user_did_save, sender=User)