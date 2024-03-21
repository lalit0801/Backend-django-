from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from user_app.api.views import registration_form,logout_view

urlpatterns=[
    path('login/',obtain_auth_token,name='login'),
    path('register/',registration_form,name='register'),
    path('logout/',logout_view,name='logout'),
]