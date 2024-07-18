from django_filters.rest_framework import FilterSet
from .models import Author,Blog

class AuthorFilter(FilterSet):
  class Meta:
    model = Author
    fields = {
      'blogs': ['exact'],
      'age': ['gt', 'lt']
    }

class BlogFilter(FilterSet):
  class Meta:
    model = Blog
    fields = {
      "category_id": ["exact"],
      "author": ["exact"]
    }