from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from .models import CartItem
from.serializers import CartItemSerializer
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from .permissions import IsOwnerOrAdmin


class CartItemViewList(generics.ListCreateAPIView):
    queryset= CartItem.objects.all()
    serializer_class= CartItemSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes= [TokenAuthentication]

    def perform_create(self, serializer):
        serializer.save(user= self.request.user)


# class CartItemDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset= CartItem.objects.all()
#     serializer_class= CartItemSerializer
#     permission_classes= [IsAuthenticated, IsOwnerOrAdmin]
#     authentication_classes= [TokenAuthentication]
    