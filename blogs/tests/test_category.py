import pytest
from django.contrib.auth.models import User
from rest_framework import status
from model_bakery import baker
from blogs.models import Category

@pytest.fixture
def create_collection(api_client):
    def inner_func(category):
        return api_client.post('/api/category/', category)
    return inner_func


@pytest.mark.django_db
class TestCreateCategory:

    def test_if_user_is_anonymous_returns_401(self, create_collection): 
        
        response = create_collection({'title': 'a'})
        
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    
    def test_if_user_is_not_admin_returns_403(self, create_collection, authenticate):
        
        authenticate()
        response = create_collection(category={'title': 'a'})

        assert response.status_code == status.HTTP_403_FORBIDDEN
    

    def test_if_data_invalid_returns_400(self, create_collection, authenticate):
        
        authenticate(is_staff=True)
        response = create_collection({'title': ''})

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data['title'] is not None


    def test_if_data_valid_returns_201(self, create_collection, authenticate):
        
        authenticate(is_staff=True)
        response = create_collection({'title': 'a'})

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['id'] > 0
 
@pytest.mark.django_db
class TestRetriveCategory:
    
    def test_if_category_exist_returns_200(self, api_client):
        category = baker.make(Category)

        response = api_client.get(f'/api/category/{category.id}/')

        assert response.status_code == status.HTTP_200_OK
        assert response.data == {
            'id' : category.id,
            'title': category.title,
            'blogs_count': 0
        } 