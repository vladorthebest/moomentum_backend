from rest_framework import serializers

from django.contrib.auth.models import User
from .models import Level

class LevelSerializer(serializers.ModelSerializer):    

    class Meta:
        model = Level
        fields = ['exp', 'lvl']
        read_only_fields = ['exp', 'lvl']
