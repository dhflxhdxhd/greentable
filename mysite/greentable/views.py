from django.shortcuts import render
from django.http import HttpResponse



def index(request):
    return HttpResponse("언제까지 반복만...?")