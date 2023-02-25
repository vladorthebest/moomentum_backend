from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Activity
from datetime import datetime, timezone
import pandas as pd

class ActivitySerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        default=serializers.CurrentUserDefault(),
        queryset=User.objects.all(),
    )

    class Meta:
        model = Activity
        fields = '__all__'
        read_only_fields = ('duration', 'activity_status')
    
    def create(self, validated_data):
        return Activity.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.activity_status = False
        time_delta = datetime.now(timezone.utc) - instance.time_start
        time_delta = pd.Timedelta(time_delta, unit ='s')
        instance.duration = time_delta.floor('S')
        instance.save()
        return instance