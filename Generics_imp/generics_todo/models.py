from django.db import models

# Create your models here.
class Task_owner_name(models.Model):
    name= models.CharField(max_length=20,unique=True)
    age= models.IntegerField()

    def __str__(self):
        return self.name

class Task(models.Model):
    
    title= models.CharField(max_length= 30, null = False, blank = False, unique = True)
    description= models.CharField(max_length= 10000)
    status= models.BooleanField(default= False)

    def __str__(self):
        return self.title
