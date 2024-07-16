from django.urls import path
from . import views



# Create your urls here.

urlpatterns = [
    path('', views.home, name="home"),
    path('docs/', views.docs, name="docs"),
    path('about/', views.about, name="about"),
    #API Views
    path('api/blogs/', views.blog_list, name="blog_list"),
    path('api/blogs/<int:id>/', views.blog_detail, name="blog_detail"),
    path('api/categories/', views.category_list, name="category_list"),
    path('api/categories/<int:id>/', views.category_detail, name="category_detail")
]

