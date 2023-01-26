from rest_framework import serializers
from .models import Profile
from django.contrib.auth.models import User

class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only = True)
    first_name = serializers.CharField(source='user.first_name', allow_blank=True,)
    last_name = serializers.CharField(source='user.last_name', allow_blank=True,)
    email = serializers.EmailField(source='user.email', allow_blank=True,)
    bio = serializers.CharField(allow_blank=True, required=False)

    class Meta:
        model = Profile
        fields = ('username', 'first_name', 'last_name', 'email', 'bio')


    def update(self, instance, validated_data):
        user_data = validated_data.pop('user', {})

        # Profile
        for (key, value) in validated_data.items():
            if value:
                setattr(instance, key, value)
        instance.save()

        # User
        for (key, value) in user_data.items():
            if value:
                setattr(instance.user, key, value)
        instance.user.save()
        
        return instance
    