from .models import Task,Task_owner_name
from rest_framework import serializers

# Create your models here.
class TaskSerializer(serializers.ModelSerializer):
    # dicounted_price= serializers.SerializerMethodField()
    class Meta:
        model= Task
        fields= [
            'title',
            'description',
            'status'
        ]
    
    


class NameSerializer(serializers.ModelSerializer):
    class Meta:
        model= Task_owner_name
        fields = '__all__'

    # def validate_title(self, value):
    #     if Task.objects.filter(title = value).exists():
    #         raise serializers.ValidationError('title should be unique')
        
    #     else :
    #         return value