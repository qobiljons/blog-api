from django.shortcuts import render, get_object_or_404
from django.db.models.aggregates import Count
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import BlogSerializer, Category_serializer
from .models import Blog, Category

# Create your views here.

def home(request):
    return render(request, 'blogs/index.html')

def docs(request):
    return render(request, 'blogs/docs.html')

def about(request):
    return render(request, 'blogs/about.html')

#API Views

@api_view()
def blog_list(request):
    queryset = Blog.objects.all()
    serializer = BlogSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view()
def blog_detail(request, id):
    blog = get_object_or_404(Blog, id=id)
    serializer = BlogSerializer(blog)
    return Response(serializer.data)

@api_view()
def category_list(request):
    queryset = Category.objects.annotate(
        blogs_count = Count('blogs')
    )
    serializer = Category_serializer(queryset, many=True)
    return Response(serializer.data)


@api_view()
def category_detail(request, id):
    category = get_object_or_404(Category.objects.annotate(
        blogs_count = Count('blogs')
    ), id=id)
    serializer = Category_serializer(category)
    return Response(serializer.data)






