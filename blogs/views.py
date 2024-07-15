from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):
    return render(request, 'blogs/index.html')

def docs(request):
    return render(request, 'blogs/docs.html')

def about(request):
    return render(request, 'blogs/about.html')

#API Views

def blogs(request):
    return HttpResponse("ok")