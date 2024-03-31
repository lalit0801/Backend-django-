# from django.db import models
# import uuid

# # Create your models here.
# class Product(models.Model):
#     name= models.CharField(max_length= 100, blank= False, null= False)
#     description= models.CharField(max_length= 1000)
#     unique_id= models.UUIDField(default=uuid.uuid4, editable= False, unique=True)
#     price= models.DecimalField(max_digits= 10, decimal_places=2, blank= False, null= False)
#     quantity= models.PositiveIntegerField(blank= False, null= False)
#     image= models.ImageField(upload_to='product_images')

#     def __str__(self):
#         return self.name
