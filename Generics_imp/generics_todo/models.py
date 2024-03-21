from django.db import models
from django.contrib.auth.models import User, AbstractUser

# Create your models here.
class Task_owner_name(models.Model):
    name= models.CharField(max_length=20,unique=True)
    age= models.IntegerField()

    def __str__(self):
        return self.name

class Task(models.Model):
    apiuser= models.ForeignKey(User, on_delete=models.CASCADE, null = False, blank = False)
    title= models.CharField(max_length= 30, null = False, blank = False, unique = True)
    description= models.CharField(max_length= 10000)
    status= models.BooleanField(default= False)

    def __str__(self):
        return self.title
    

# class CustomUser(AbstractUser):
#     is_admin = models.BooleanField(default = False)
#     def __str__(self):
#         return self.username

# class customtaskowner(AbstractUser):
#     is_task_creator= models.BooleanField(default=False)
    