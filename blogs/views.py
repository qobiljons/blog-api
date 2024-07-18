from django.shortcuts import render, get_object_or_404
from django.db.models.aggregates import Count
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.mixins import ListModelMixin
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from .serializers import AuthorSerializer, BlogSerializer, CategorySerializer, ReviewSerializer
from .models import Blog, Category, Author, Review


# Create your views here.

def home(request):
    return render(request, 'blogs/index.html')

def docs(request):
    return render(request, 'blogs/docs.html')

def about(request):
    return render(request, 'blogs/about.html')

def custom_404(request):
    return render(request, 'blogs/404.html')


#API Views
class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.select_related('user').annotate(blogs_count = Count('blogs'))
    serializer_class = AuthorSerializer


class BlogViewSet(ModelViewSet):
    queryset = Blog.objects.select_related("author", "category").prefetch_related("reviews").order_by("-created_at")
    serializer_class = BlogSerializer
    


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.annotate(blogs_count = Count('blogs')).order_by('-id')
    serializer_class = CategorySerializer
    
    def destroy(self, request, *args, **kwargs):
        if Blog.objects.filter(category__id = kwargs["pk"]):
            return Response({"error": "Cannot delete a category with associated blogs"}, status=status.HTTP_405_METHOD_NOT_ALLOWED) 
        return super().destroy(request, *args, **kwargs)
    
class ReviewViewSet(ModelViewSet):
    def get_queryset(self):
        return Review.objects.select_related('author').filter(blog_id=self.kwargs['blog_pk'])
    serializer_class = ReviewSerializer

    def get_serializer_context(self):
        return {
            "blog_id" : self.kwargs["blog_pk"],
            "author`": self.request.user
        }
