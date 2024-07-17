from django.urls import path, include
from . import views
from rest_framework.routers import SimpleRouter, DefaultRouter

router = DefaultRouter()
router.register("authors", views.AuthorViewSet)
router.register("category", views.CategoryViewSet)
router.register("blogs", views.BlogViewSet)



# Create your urls here.

urlpatterns = [
    path('', views.home, name="home"),
    path('docs/', views.docs, name="docs"),
    path('about/', views.about, name="about"),
    path('api/', include(router.urls))
] 


