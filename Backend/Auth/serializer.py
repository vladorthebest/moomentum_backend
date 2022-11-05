from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(label="username", write_only=True)
    password = serializers.CharField(label="password", write_only=True)

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        user = authenticate(request=self.context.get('request'), username=username, password=password)
        if user is None:
            raise serializers.ValidationError(
                'A user with this username and password is not found.'
            )
        attrs['user'] = user
        return attrs
    
class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required = True, 
        validators = [UniqueValidator(queryset=User.objects.all())]
        )
    password = serializers.CharField(
        required = True, 
        write_only = True,
        validators = [validate_password]
        )
    password2 = serializers.CharField(
        required = True, 
        write_only = True
        )

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'password2', 'email')
        read_only_fields = ('id',)


    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username = validated_data['username'],
            email = validated_data['email']
        )

        user.set_password(validated_data['password'])
        user.save()
        return user