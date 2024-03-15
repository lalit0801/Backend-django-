from rest_framework import generics
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer

class TaskCreateAPIView(generics.CreateAPIView):
    # queryset = Task.objects.all()
    serializer_class = TaskSerializer

    
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


class TaskUpdateAPIView(generics.UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

task_update_view= TaskUpdateAPIView.as_view()

class TaskDestroyAPIView(generics.DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

task_destroy_view= TaskDestroyAPIView.as_view()