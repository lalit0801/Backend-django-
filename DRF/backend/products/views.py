from rest_framework import generics

from .models import Product
from .serializers import ProductSerializer


class ProductCreateAPIView(generics.CreateAPIView):
    queryset= Product.objects.all()
    serializer_class= ProductSerializer

    def perform_create(self, serializer):
        return super().perform_create(serializer)


product_create_view= ProductCreateAPIView.as_view()
    

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset= Product.objects.all()
    serializer_class= ProductSerializer


product_detail_view= ProductDetailAPIView.as_view()