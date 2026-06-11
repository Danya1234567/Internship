from django.contrib.auth import authenticate
from rest_framework import serializers

from user.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','username','email','password','created_at','verified']
        read_only_fields=['created_at']

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','email','password']
        extra_kwargs={'password':{'write_only':True}}

    def create(self,validated_data):
        user=User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'])
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)
    def validate(self,data):
        user=authenticate(username=data['username'],password=data['password'])
        if not user:
            raise serializers.ValidationError('Not a valid username or password')
        data['user']=user
        return data