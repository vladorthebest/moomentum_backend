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
        read_only_fields = ('duration', 'activity_status', 'exp')
    
    def create(self, validated_data):
        return Activity.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.activity_status = False

        time_delta = datetime.now(timezone.utc) - instance.time_start
        time_delta = pd.Timedelta(time_delta, unit ='s')
        time_delta_minutes = time_delta.total_seconds()/60

        if(time_delta_minutes < 1):
            instance.delete()
            return serializers.ValidationError('Less than a minute activity cannot be')
        instance.duration = time_delta.floor('S')
        instance.exp = time_delta_minutes
        instance.save()
        return instance