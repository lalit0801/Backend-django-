from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response
from user_app.api.serializers import registerserializer
from rest_framework import status
from user_app import models
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication

@api_view(['POST',])
def registration_form(request):
    if request.method== 'POST':
        serializer= registerserializer(data= request.data)
        print("working1")
        if serializer.is_valid():
            print("working2")
            serializer.save()
            print("working3")
            return Response(serializer.data,status=status.HTTP_201_CREATED)

@api_view(['POST',])
@authentication_classes([TokenAuthentication])
def logout_view(request):
      if request.method=='POST':
         request.user.auth_token.delete()
         return Response(status= status.HTTP_200_OK)  
                