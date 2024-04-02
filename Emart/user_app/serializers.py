from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import authenticate

class UserSerializer(serializers.ModelSerializer):
    password= serializers.CharField(max_length=128, min_length = 8, write_only=True)
    class Meta:
        model= CustomUser
        fields= ['email', 'password', 'is_admin', 'is_registered', 'id','username']
        read_only_fields= ['id']
    


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

