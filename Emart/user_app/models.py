from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

# Create your models here.
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, blank=False, null=False)
    password= models.CharField(max_length=150, unique=True)
    is_admin = models.BooleanField(default = False)
    is_registered = models.BooleanField(default = False)
    unique_id= models.UUIDField(default=uuid.uuid4, editable= False, unique=True)
    username = models.CharField(max_length=50, blank=False, null = False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username
