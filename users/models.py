
from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from PIL import Image

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
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
    
    def save(self):
        super().save()

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            ouput_size = (300, 300)
            img.thumbnail(ouput_size)
            img.save(self.image.path)

def user_did_save(sender, instance, created, *args, **kwargs):
    if created:
        Profile.objects.get_or_create(user=instance)

post_save.connect(user_did_save, sender=User)