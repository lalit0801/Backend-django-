from django.forms.models import model_to_dict
# from django.http import JsonResponse
from products.models import Product
from rest_framework.response import Response
from rest_framework.decorators import api_view
# serializer


@api_view(["GET"])
def apihome(request, *args, **kwargs):
    model_data= Product.objects.all().order_by("?").first()
    data={}
    if model_data:
        data= model_to_dict(model_data, fields=['id','title','price','sale_price'])

    return Response(data)
