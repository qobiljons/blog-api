from django.shortcuts import render, get_object_or_404
from django.db.models.aggregates import Count
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
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
@api_view(["GET", "POST"])
def author_list(request):
    if request.method == "GET":
        queryset = Author.objects.select_related('user').annotate(
            blogs_count = Count('blogs')
        )
        serializer = AuthorSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = AuthorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(["GET", "PATCH", "DELETE"])
def author_detail(request, id):
    author = get_object_or_404(Author.objects.annotate(
        blogs_count = Count('blogs')
    ), id=id)
    if request.method == "GET":
        serializer = AuthorSerializer(author)
        return Response(serializer.data)
    elif request.method == "PATCH":
        serializer = AuthorSerializer(author, request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status = status.HTTP_200_OK)
    elif request.method == "DELETE":
        author.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)


@api_view(["GET", "POST"])
def blog_list(request):
    if request.method == "GET":
        queryset = Blog.objects.all().order_by("created_at")
        serializer = BlogSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = BlogSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    

@api_view(["GET", "PATCH", "DELETE"])
def blog_detail(request, id):
    blog = get_object_or_404(Blog, id=id)
    if request.method == "GET":
        serializer = BlogSerializer(blog)
        return Response(serializer.data)
    elif request.method == "PATCH":
        serializer = BlogSerializer(blog, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "DELETE":
        blog.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
    

@api_view(["GET", "POST"])
def category_list(request):
    if request.method == "POST":
        serializer = CategorySerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    queryset = Category.objects.annotate(
        blogs_count = Count('blogs')
    )
    serializer = CategorySerializer(queryset, many=True)
    return Response(serializer.data)


@api_view(["GET", "PATCH", "DELETE"])
def category_detail(request, id):
    category = get_object_or_404(Category.objects.annotate(
        blogs_count = Count('blogs')
    ), id=id)
    if request.method == "PATCH":
        serializer = CategorySerializer(category, data = request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status = status.HTTP_200_OK)
    elif request.method == "DELETE":
        if category.blogs.count() > 0:
            return Response({"error": "Cannot delete a category with associated blogs"}, status=status.HTTP_405_METHOD_NOT_ALLOWED) 
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
    serializer = CategorySerializer(category)
    return Response(serializer.data)






