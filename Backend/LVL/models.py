from django.db import models


from django.contrib.auth.models import User


class Level(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    lvl = models.IntegerField(default=1)
    exp = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username
