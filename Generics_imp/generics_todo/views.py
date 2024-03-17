from rest_framework import generics
from rest_framework.response import Response
from .models import Task, Task_owner_name 
from .serializers import TaskSerializer, NameSerializer
from  rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .permission import OurAuthenticationPermissions

class testView(APIView):
    def get(self, request):
        details= Task_owner_name.objects.all()
        serializer = NameSerializer(details, many= True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = NameSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else :
            return Response(serializer.errors)

class testdetail(APIView):

    def get(self, request, pk):
        details= Task_owner_name.objects.get(pk=pk)
        serializer= NameSerializer(details)
        return Response(serializer.data)


class TaskCreateAPIView(generics.CreateAPIView):
    # queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, IsAuthenticatedOrReadOnly]
    
    # 
    # fun():
    # obj = TaskCreateAPIView
    # obj.queryset= mslmef
    # obj.sefs = skensl

    # obj.get_queryset(self)
    # return self.queryset

    # obj.get_serializer(self())
    #         self.selrlclass
    
    # obj.post(self, request, keawws)
    #     DATA = REQUEST.DATA
    #     serializr(data)


class TaskViewAllAPIView(generics.ListAPIView):
    # queryset = Task.objects.filter().first()
    serializer_class = TaskSerializer
    permission_classes = [OurAuthenticationPermissions]
    
    def get_queryset(self):
        des = self.kwargs['des']
        return Task.objects.filter(description = des)

# task_viewall_view= TaskViewallAPIView.as_view()

# class TaskDetailAPIView(generics.RetrieveAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer
    
#     def list(self, request, *args, **kwargs):
#         queryset = self.get_queryset()
#         serializer = self.get_serializer(queryset, many=True)
#         return Response(serializer.data)

# task_detail_view= TaskDetailAPIView.as_view()


class TaskUpdateAPIView(generics.UpdateAPIView, ):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

task_update_view= TaskUpdateAPIView.as_view()

class TaskDestroyAPIView(generics.DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

task_destroy_view= TaskDestroyAPIView.as_view()