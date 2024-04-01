from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import authenticate

class UserSerializer(serializers.ModelSerializer):
    password= serializers.CharField(max_length=128, min_length = 8, write_only=True)
    class Meta:
        model= CustomUser
        fields= ['email', 'password', 'is_admin', 'is_registered', 'unique_id','username']
        read_only_fields= ['unique_id']
    

# class LoginSerializer(serializers.Serializer):
#     email = serializers.EmailField()
#     password = serializers.CharField()

#     def validate(self, data):
#         email = data.get('email')
#         password = data.get('password')

#         # Check if email and password are provided
#         if not email or not password:
#             raise serializers.ValidationError('Email and password are required')

#         # Authenticate user
#         user = authenticate(email=email, password=password)

#         if not user:
#             raise serializers.ValidationError('Invalid email or password')

#         # If authentication is successful, return the validated data
#         data['user'] = user
        # return data