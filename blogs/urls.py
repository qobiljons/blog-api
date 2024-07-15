from django.urls import path
from . import views


# Create your urls here.

urlpatterns = [
    path('', views.home, name="home"),
    path('docs/', views.docs, name="docs"),
    path('about/', views.about, name="about"),
    #API Views
    path('api/blogs/', views.blogs, name="blogs"),
]