from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

# Create your models here.
class CustomUser(AbstractUser):
    # image = models.ImageField(upload_to = "profile/", blank=True, null = True)
    email = models.EmailField(unique=True, blank=False, null=False)
    password= models.CharField(max_length=128)
    is_admin = models.BooleanField(default = False)
    is_registered = models.BooleanField(default = False)
    id= models.UUIDField(primary_key= True, default=uuid.uuid4, editable= False, unique=True)
    username = models.CharField(unique=True,max_length=50, blank=False, null = False)
    

    def __str__(self):
        return self.username
