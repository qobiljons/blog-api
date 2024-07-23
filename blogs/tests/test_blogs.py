import pytest
from django.contrib.auth.models import User
from rest_framework import status
from model_bakery import baker
from blogs.models import Blog

@pytest.fixture
def create_blog():
    pass


@pytest.fixture
def create_invalid_blog():
    pass


pytest.mark.django_db
class TestCreateBlogs:
    pass
