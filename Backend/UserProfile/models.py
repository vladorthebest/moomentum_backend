from django.db import models
from django.contrib.auth.models import User

from django.dispatch import receiver
from django.db.models.signals import post_save

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    
    def __str__(self):
        return self.user.username

# post_save.connect(user_created_handler, sender=User) or receiver
@receiver(post_save, sender=User)
def user_created_handler(sender, instance, created, *args, **kwargs):
    if created:
        Profile.objects.create(user=instance)