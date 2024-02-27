from django.http import JsonResponse

def apihome(request, *args, **kwargs):
    return JsonResponse({"message":"this is django api response!!"})
