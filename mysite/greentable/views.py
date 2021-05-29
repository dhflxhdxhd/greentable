from django.shortcuts import render
from .models import Place
# from django.http import HttpResponse

def index(request):
    Places = Place.objects.all()

    context = {
        'Places' : Places,
    }
    return render(request,'index.html',context=context)


def result(request):

    return render(request, 'index.html')