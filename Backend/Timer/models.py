from django.db import models
from django.contrib.auth.models import User

class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    time_start = models.DateTimeField(auto_now=True)
    duration = models.DurationField(null=True, blank=True)
    activity_status = models.BooleanField(default=True)