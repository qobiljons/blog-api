from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import BlogSerializer
from .models import Blog

# Create your views here.

def home(request):
    return render(request, 'blogs/index.html')

def docs(request):
    return render(request, 'blogs/docs.html')

def about(request):
    return render(request, 'blogs/about.html')

#API Views

@api_view(["GET"])
def blog_list(request):
    queryset = Blog.objects.all()
    serializer = BlogSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view()
def blog_detail(request, id):
    blog = get_object_or_404(Blog, id=id)
    serializer = BlogSerializer(blog)
    return Response(serializer.data)

