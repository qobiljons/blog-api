from django.shortcuts import render, get_object_or_404
from django.db.models.aggregates import Count
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import AuthorSerializer, BlogSerializer, CategorySerializer
from .models import Blog, Category, Author


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

class AuthorList(APIView):
    def get(self, request):
        queryset = Author.objects.select_related('user').annotate(
            blogs_count = Count('blogs')
        )
        serializer = AuthorSerializer(queryset, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = AuthorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

class AuthorDetail(APIView):
    def get(self, request, *args, **kwargs):
        author = get_object_or_404(Author.objects.annotate(
            blogs_count = Count('blogs')
        ), id=kwargs["id"])
        serializer = AuthorSerializer(author)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        author = get_object_or_404(Author.objects.annotate(
        blogs_count = Count('blogs')
        ), id=kwargs["id"])
        serializer = AuthorSerializer(author, request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status = status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        author = get_object_or_404(Author.objects.annotate(
        blogs_count = Count('blogs')
        ), id=kwargs["id"])
        author.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
    

class BlogList(APIView):
    def get(self, request):
        queryset = Blog.objects.all().prefetch_related("reviews").order_by("-created_at")
        serializer = BlogSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = BlogSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    

class BlogDetail(APIView):
    def get(self, request, *args, **kwargs):
        blog = get_object_or_404(Blog, id=kwargs["id"])
        serializer = BlogSerializer(blog)
        return Response(serializer.data)

    def patch(self, request, *args, **kwargs):
        blog = get_object_or_404(Blog, id=kwargs["id"])
        serializer = BlogSerializer(blog, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        blog = get_object_or_404(Blog, id=kwargs["id"])
        blog.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
    


class CategoryList(APIView):
    def get(self, request):
        queryset = Category.objects.annotate(blogs_count = Count('blogs')).order_by('-id')
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)


class CategoryDetail(APIView):
    def get(self, request, *args, **kwargs):
        category = get_object_or_404(Category.objects.annotate(
            blogs_count = Count('blogs')
        ), id=kwargs["id"])

        serializer = CategorySerializer(category)
        return Response(serializer.data)


    def patch(self, request, *args, **kwargs):
        category = get_object_or_404(Category.objects.annotate(
            blogs_count = Count('blogs')
        ), id=kwargs["id"])
        serializer = CategorySerializer(category, data = request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status = status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        category = get_object_or_404(Category.objects.annotate(
            blogs_count = Count('blogs')
        ), id=kwargs["id"])
        if category.blogs.count() > 0:
            return Response({"error": "Cannot delete a category with associated blogs"}, status=status.HTTP_405_METHOD_NOT_ALLOWED) 
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)








