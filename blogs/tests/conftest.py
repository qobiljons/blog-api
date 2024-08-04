import pytest
from rest_framework.test import APIClient
from django.contrib.auth.models import User


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def authenticate(api_client):
    def inner_func(is_staff=False):
        return api_client.force_authenticate(user=User(is_staff=is_staff))
    return inner_func


@pytest.fixture
def create_collection(api_client):
    def inner_func(category):
        return api_client.post('/api/category/', category)
    return inner_func



