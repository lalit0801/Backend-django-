from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response
from user_app.api.serializers import registerserializer
from rest_framework import status
from user_app import models
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication

@api_view(['POST',])
def registration_form(request):
    if request.method== 'POST':
        serializer= registerserializer(data= request.data)
        print("working1")
        data={}
        if serializer.is_valid():
            print("working2")
            account= serializer.save()
            data['username']= account.username
            data['email']= account.email
            # token= Token.objects.get(user=account).key
            refresh= RefreshToken.for_user(account)
            data['token']= {
                'refresh': str(refresh),
                'access':str(refresh.access_token ),
            }
        else:
            data= serializer.errors

            print("working3")
        return Response(data,status=status.HTTP_201_CREATED)

@api_view(['POST',])
@authentication_classes([TokenAuthentication])
def logout_view(request):
      if request.method=='POST':
         request.user.auth_token.delete()
         return Response(status= status.HTTP_200_OK)  
                