from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model= Product
        fields = [
            'title',
            'content',
            'price',
            'sale_price',
            'my_discount'
        ]

    # def validate_empty_values(self, data):
    #    return super().validate_empty_values(data)
    # def validate_title(self, title):
    #     if Product.objects.filter(title = attrs['title']).exists():
    #       raise serializers.ValidationError('title should be uniqe')

    #     if attrs['title'] == 'sumit':
    #       raise serializers.ValidationError('you cannot ass sumit as your title')
        
    #     return hash(passs)
    
    # def validate(self, attrs):
      
       
    #    return super().validate(attrs)
    

    def get_my_discount(self, obj):
      if not hasattr(obj,'id'):
        return None
      if not isinstance(obj,Product):
         return None
      return obj.get_discount()
     
    