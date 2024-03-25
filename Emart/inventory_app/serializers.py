from rest_framework import serializers
from . models import Product

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model= Product
        field=[
            'name', 'unique_id', 'price', 'stock', 'image'
        ]