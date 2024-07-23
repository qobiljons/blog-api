from django.shortcuts import render
from django.db.models.aggregates import Count
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet
from rest_framework.mixins import  RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from .serializers import AuthorSerializer, BlogSerializer, CategorySerializer, ReviewSerializer, BlogImageSerializer
from .models import Blog, Category, Author, Review, BlogImage
from .filters import BlogFilter
from .pagination import DefaultPagination
from .permissions import IsOwnerOrReadOnly, IsAdminOrReadOnly, IsAuthorOrReadOnly, IsBlogOwnerOrReadOnly

# Create your views here.

def home(request):
    return render(request, 'blogs/index.html')

def docs(request):
    return render(request, 'blogs/docs.html')

def about(request):
    return render(request, 'blogs/about.html')

def custom_404(request):
    return render(request, 'blogs/404.html')

# API Views
class AuthorViewSet(
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    ListModelMixin,
    GenericViewSet
):
    queryset = Author.objects.select_related('user').annotate(blogs_count=Count('blogs'))
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthorOrReadOnly]
    
    @action(detail=False, methods=["GET",  "PUT"])
    def me(self, request):
        author = Author.objects.get(user_id=request.user.id)

        if request.method == 'GET':
            serializer = AuthorSerializer(author)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = AuthorSerializer(author, data = request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)


class BlogViewSet(ModelViewSet):
    queryset = Blog.objects.select_related("author", "category").prefetch_related("reviews", "images").order_by("-created_at")
    serializer_class = BlogSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = BlogFilter
    pagination_class = DefaultPagination
    permission_classes = [IsOwnerOrReadOnly]
    search_fields = ["title"]
    ordering_fields = ["title", "id"]

    def get_serializer_context(self):
        if self.request.method == "POST":
            return {
                "author": self.request.user.author
            }
        return super().get_serializer_context()
        
class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.annotate(blogs_count=Count('blogs')).order_by('-id')
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]
    
    def destroy(self, request, *args, **kwargs):
        if Blog.objects.filter(category__id=kwargs["pk"]).exists():
            return Response({"error": "Cannot delete a category with associated blogs"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        return super().destroy(request, *args, **kwargs)


class ReviewViewSet(ModelViewSet):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.select_related('author').filter(blog_id=self.kwargs['blog_pk'])

    def get_serializer_context(self):
        return {
            "blog_id": self.kwargs["blog_pk"],
            "author": self.request.user
        }
    
class BlogImageViewSet(ModelViewSet):
    serializer_class = BlogImageSerializer
    permission_classes = [IsBlogOwnerOrReadOnly]
    def get_serializer_context(self):
        return {
            "blog_id": self.kwargs["blog_pk"]
        }
    
    def get_queryset(self):
        return BlogImage.objects.filter(blog_id=self.kwargs['blog_pk'])
    

