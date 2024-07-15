from django_filters.rest_framework import FilterSet
from .models import Author

class AuthorFilter(FilterSet):
  class Meta:
    model = Author
    fields = {
      'blogs': ['exact'],
      'age': ['gt', 'lt']
    }