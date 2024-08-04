import pytest
from django.contrib.auth.models import User
from rest_framework import status
from model_bakery import baker
from blogs.models import Blog, Author
from core.models import CustomUser


@pytest.fixture
def create_blog(api_client):
    def inner_function(blog):
        return api_client.post('api/blogs/', blog)
    return inner_function


@pytest.mark.django_db
class TestCreateBlogs:   
    def test_if_user_is_anonymous_returns_401(self):
        print(blog.__dic__)
        assert False

