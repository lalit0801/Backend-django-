from django.urls import path
from . import views

urlpatterns=[
    path('', views.home, name='home'),
    path('create/', views.create, name='create'),  #http://localhost:8000/list_single
    path('list_all/', views.list_all, name='list_all'),
    path('list_single/<str:task_id>/', views.list_single, name='list_single'),
    path('update/', views.update, name='update'),
    path('delete/<str:task_id>/', views.delete, name='delete'),
    path('status/', views.status, name='status'),

]