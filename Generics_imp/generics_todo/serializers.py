from .models import Task
from rest_framework import serializers

# Create your models here.
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model= Task
        fields= [
            'title',
            'description',
            'status'
        ]

    # def validate_title(self, value):
    #     if Task.objects.filter(title = value).exists():
    #         raise serializers.ValidationError('title should be unique')
        
    #     else :
    #         return value