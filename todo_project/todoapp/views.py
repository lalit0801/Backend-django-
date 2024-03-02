from django.shortcuts import render
from django.http import JsonResponse
from .models import Task
import json

# Create your views here.
def home(request):
    return JsonResponse({'message':'Welcome to the home page of Todo project'})

# operations:: Create, list_all, list_single, edit/update, delete , change status

def list_all(request):
   try: 
    tasks= Task.objects.all().values()
    print(tasks)
    print(type(tasks))
    return JsonResponse({'message': list(tasks)}, status =200)
   except Exception as e:
      return JsonResponse({'message': 'exception occured'}, status= 400) 
    # print(Task.objects.get(id=1))
    # print(type(Task.objects.get(id=1)))
    # print(Task.objects.all())
    # print(type(Task.objects.all()))
    # tasks = Task.objects.all()
    # tasks = Task.objects.all().values()   {{obj1},{obj2},{obj3}}
    # {
    #  {
    #      'id':1,
    #      'title':'a',
    #      'description':'b',
    #      'status': True,
    #      'created_at': 2024-02-29,
    #      'updated_at': 2024-01-02
    
    #  },
    #  {
    #      'id':2,
    #      'title':'title2',
    #      'description':'desc2',
    #      'status': False,
    #      'created_at': 2023-02-29,
    #      'updated_at': 2023-01-02
    #  },
    #  {
    #      'id':3,
    #      'title':'title3',
    #      'description':'desc3',
    #      'status': True,
    #      'created_at': 2022-02-29,
    #      'updated_at': 2022-01-02
    #  }
    #  }
    # print(tasks)
    # data={}
    # i=0
    # for task in tasks:
    #     data.append({i:task})
    #     i++
    # return JsonResponse({'message': tasks})
   

def list_single(request,task_id):
   try: 
    #  print(kwargs)
    #  print(type(kwargs))
    # task_id= kwargs.get('task_id')
    
     print(task_id)
     if request.method== 'GET':
      task= Task.objects.filter(id= task_id).values().first()
      print(task)
      print(type(task))
      if not task:
         return JsonResponse({'message':'Task with this id not found'},status= 400)
      return JsonResponse({'message': task},status=200)
     return JsonResponse({'message':'only POST requests allowed'},status=400)
   except Exception as e:
      return JsonResponse({'messgae':'error occurred'},status=400)


def create(request):
  try:
    print('################')
    if request.method== 'POST':
        task_data= json.loads(request.body)
        print(task_data)
        print(type(task_data))
        # raise Exception('exception raised on purpose')
        if not task_data.get('title'):
            return JsonResponse({'message':'Title cannot be empty'},status=400)
        if Task.objects.filter(title= task_data['title']).exists():
            return JsonResponse({'message':'title already exists'},status=400)
        task= Task.objects.create(title= task_data['title'],description= task_data.get('description',''), status= task_data.get('status', False))
        print(type(task))
        return JsonResponse({'message':{'id':task.id,'title':task.title,'description':task.description,'status':task.status}},status=200)
        
    return JsonResponse({'message':'only POST requests allowed'},status=400)
  except Exception as e: 
    #  print(type(e))
     return JsonResponse({'message': str(e)},status= 400)


def delete(request,task_id):
  try:
    if request.method=='GET':
     if not task_id:
         return JsonResponse({'message': 'Task id is missing or required'}, status=400)
     task= Task.objects.get(id= task_id)
     print(task)
     print(type(task))
     if not task:
        return JsonResponse({'message': 'task with this id not found'}, status=400)
     task.delete()
     return JsonResponse({'message':'task deleted successfully'},status=200)
    return JsonResponse({'message':'only POST requests allowed'},status=400)
  except Exception as e:
     return JsonResponse({'message':'error occured'},status= 400)

def status(request):
  try:
    if request.method=='POST':
      task_id = request.POST['id'] 

      if not task_id:
         return JsonResponse({'message':'id is required field'},status=400)
      task = Task.objects.filter(id=task_id).first()
      print(task)
      print(type(task))
      if not task:
        return JsonResponse({'message': 'Task not found'}, status=400)
      task.status = True
      task.save()
      return JsonResponse({'message': 'Task marked as completed'},status =200)
    return JsonResponse({'message':'only POST requests allowed'},status=400)
  except Exception as e:
     return JsonResponse({'message':'error occured'},status= 400)
  
def update(request):
   try: 
      if request.method=='GET':
         print("aaa")

         data= json.loads(request.body)
         task_id= data['id']
         print("bbb",task_id)
         task= Task.objects.filter(id= task_id).values().first()
         print(task)
         if not task:
            return JsonResponse({'message':'task with this id not found'},status=400)
         taskobj= Task.objects.get(id=task_id)
         updated_data= data

         taskobj.title= updated_data.get('title',taskobj.title)
         taskobj.description= updated_data.get('description',taskobj.description)
         taskobj.status=updated_data.get('status',taskobj.status)
         taskobj.save()
         print(taskobj)
         return JsonResponse({'message':'task has been updated'},status=200)
      return JsonResponse({'message':'only POST requests allowed'},status=400)
   except Exception as e:
      return JsonResponse({'message':str(e)},status=400)