from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save


from django.contrib.auth.models import User
from Timer.models import Activity

class Level(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    lvl = models.IntegerField(default=1)
    exp = models.IntegerField(default=0)
    exp_start = models.IntegerField(default=0)
    exp_finish = models.IntegerField(default= int((1 * 10) ** 1.334))

    def __str__(self):
        return self.user.username

    def add_exp(self, exp):
        self.exp += exp
        if (self.exp >= self.exp_finish):
            self.up_level()
    
    def up_level(self):
        self.lvl += 1
        self.exp_start = self.exp_finish
        self.exp_finish = self.calc_next_lvl()
    
    def calc_next_lvl(self): 
        return int((self.lvl * 10) ** 1.334)


@receiver(post_save, sender=User)
def user_created_handler(sender, instance, created, *args, **kwargs):
    if created:
        instance_level = Level.objects.create(user=instance)
    
@receiver(post_save, sender=Activity)
def user_created_handler(sender, instance, created, *args, **kwargs):
    if not created:
        instance_level = Level.objects.get(user=instance.user)
        instance_level.add_exp(instance.exp)
        instance_level.save()