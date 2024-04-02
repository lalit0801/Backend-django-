from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from .models import CustomUser
from .utils import create_token, delete_token
from .serializers import UserSerializer, LoginSerializer
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication


class RegisterView(generics.CreateAPIView):
    queryset= CustomUser.objects.all()
    serializer_class= UserSerializer
    


class LoginView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class= LoginSerializer
    
    
    def post(self, request):
        try:
            print(request.data)
            
            
            email = request.data.get('email')
            password = request.data.get('password')
            print('0')
            if not CustomUser.objects.filter(email=email).exists():
             return Response({ 'message': 'email not found'}, status=400)
        
            

            user = CustomUser.objects.get(email=email)
            print(user)
            print(password)
            if  user.password!=password:
              return Response({ 'message': 'Incorrect password'}, status=400)
        
            print('2')
            
            token, created = Token.objects.get_or_create(user=user)
            print('3')
            return Response({'status': True, 'token': token.key}, status=200)
            
                

        except CustomUser.DoesNotExist:
            return Response({'status': False, 'message': 'User not found'}, status=400)
        except Exception as e:
            return Response({'status': False, 'message': str(e)}, status=400)

class LogoutView(generics.RetrieveAPIView):
    def get(self, request):
        auth_header = request.headers.get('Authorization')
        if auth_header and auth_header.startswith('Token '):
            token = auth_header.split(' ')[1]

            try:
                token = Token.objects.get(key=token)
                token.delete()
                return Response({'status': True, 'message': 'User Logout Successfully'}, status=200)
            except Token.DoesNotExist:
                return Response({'status': False, 'message': 'Invalid token'}, status=400)
        
        else:
            return Response({'status': False, 'message': 'Missing Token'}, status=400)




# class RegisterView(GenericAPIView):
#     serializer_class = UserSerializer

#     def post(self, request, *args, **kwargs):
#         try:
#             serializer = self.get_serializer(data=request.data)
#             serializer.is_valid(raise_exception=True)
#             user = serializer.save()  # Creates a new user
#             return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
#         except Exception as e:
#             return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
# class LoginView(GenericAPIView):
#     serializer_class = LoginSerializer

#     def post(self, request, *args, **kwargs):
#         try:
#             serializer = self.get_serializer(data=request.data)
#             serializer.is_valid(raise_exception=True)
#             user = authenticate(email=serializer.validated_data['email'], password=serializer.validated_data['password'])
#             if user:
#                 token = create_token(user)
#                 return Response({'token': token.key}, status=status.HTTP_200_OK)
#             else:
#                 return Response({'error': 'Invalid email or password'}, status=status.HTTP_400_BAD_REQUEST)
#         except Exception as e:
#             return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
# class LogoutView(GenericAPIView):

#     def post(self, request, *args, **kwargs):
#         try:
#             # Delete the user's authentication token
#             delete_token(request.user)
#             return Response({'message': 'User logged out successfully'}, status=status.HTTP_200_OK)
#         except Exception as e:
#             return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)