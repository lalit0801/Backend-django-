

from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router= DefaultRouter()
router.register('list',views.list_viewset,basename='showroom')


urlpatterns=[
    
    path('create/', views.TaskCreateAPIView.as_view()),  #http://localhost:8000/list_single
    # path('list/<str:des>/', views.TaskViewAllAPIView.as_view()),
    # path('list_single/<str:pk>/', views.task_detail_view),
    path('', include(router.urls) ),
    path('update/<str:pk>/', views.task_update_view),
    path('delete/<str:pk>/', views.task_destroy_view),
    

]