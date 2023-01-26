from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save


from django.contrib.auth.models import User
from Timer.models import Activity

class Level(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    lvl = models.IntegerField(default=1)
    exp = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def user_created_handler(sender, instance, created, *args, **kwargs):
    if created:
        Level.objects.create(user=instance)
    
@receiver(post_save, sender=Activity)
def user_created_handler(sender, instance, created, *args, **kwargs):
    if not created:
        instance_profile = Level.objects.get(user=instance.user)
        instance_profile.exp += instance.exp
        instance_profile.save()