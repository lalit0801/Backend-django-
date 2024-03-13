from django.forms.models import model_to_dict
# from django.http import JsonResponse
from products.models import Product
from rest_framework.response import Response
from rest_framework.decorators import api_view

# serializer
from products.serializers import ProductSerializer


@api_view(["POST"])
def apihome(request, *args, **kwargs): 
    serializer = ProductSerializer(data = request.data)
    serializer = ProductSerializer(model_object)
    serializer = ProductSerializer(model_object, data = {})
    
    serializer.is_valid(raise_exception=True)
    model_object = serializer.save()
    print("##########################")
    # print(data, "******")
    # print(serializer.data)
    data = serializer.data
    # print(data)
    # print(type(data))

    # print(type(data), "******")
    # try :
    #     print(updated_object.data)
    #     updated_object.is_valid(raise_exception=True)
    #     obj = updated_object.save()
    # except Exception as e:
    #     print(str(e))


    print(model_object.title)
    # instance= Product.objects.all().order_by("?").first()
    # data={}
    # if instance:
    #     # data= model_to_dict(instance, fields=['id','title','price','sale_price'])
    #       data= ProductSerializer(instance).data
    return Response(data)

