from django.shortcuts import render
from django.http import HttpResponse
from . models import Feature

# Create your views here.
def index(request):
    feature1 = Feature()
    feature1.id = 0
    feature1.name = 'lalit'
    feature1.details= 'i am optimus'

    feature2 = Feature()
    feature2.id = 1
    feature2.name = 'lalit'
    feature2.details= 'i am optimus'

    feature3 = Feature()
    feature3.id = 2
    feature3.name = 'lalit'
    feature3.details= 'i am optimus'

    feature4 = Feature()
    feature4.id = 3
    feature4.name = 'lalit'
    feature4.details= 'i am optimus'

    features =[feature1, feature2, feature3, feature4]
    return render(request,'index.html',{'features': features})

def counter(request):
    text=request.POST['text']
    amount_of_words = len(text.split())
    return render(request,'counter.html',{'amount': amount_of_words})

