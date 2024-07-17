from django.urls import path
from . import views



# Create your urls here.

urlpatterns = [
    path('', views.home, name="home"),
    path('docs/', views.docs, name="docs"),
    path('about/', views.about, name="about"),
    #API Views
    path('api/authors', views.AuthorList.as_view(), name = "author_list"),
    path('api/authors/<int:id>', views.AuthorDetail.as_view(), name="author_detail"),
    path('api/blogs/', views.BlogList.as_view(), name="blog_list"),
    path('api/blogs/<int:id>/', views.BlogDetail.as_view(), name="blog_detail"),
    path('api/categories/', views.CategoryList.as_view(), name="category_list"),
    path('api/categories/<int:id>/', views.CategoryDetail.as_view(), name="category_detail"),
    path('404/', views.custom_404, name="404")
]


