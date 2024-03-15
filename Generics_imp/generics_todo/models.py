from django.db import models

# Create your models here.
class Task(models.Model):
    
    title= models.CharField(max_length= 30, null = False, blank = False, unique = True)
    description= models.CharField(max_length= 10000)
    status= models.BooleanField(default= False)
