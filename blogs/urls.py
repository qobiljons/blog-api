from django.urls import path, include
from . import views
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register("authors", views.AuthorViewSet)
router.register("category", views.CategoryViewSet)
router.register("blogs", views.BlogViewSet, basename="blogs")

blogs_router = routers.NestedDefaultRouter(router, "blogs", lookup="blog")
blogs_router.register('reviews', views.ReviewViewSet, basename="blog-reviews")



# Create your urls here.

urlpatterns = [
    path('', views.home, name="home"),
    path('docs/', views.docs, name="docs"),
    path('about/', views.about, name="about"),
    path('api/', include(router.urls)),
    path('api/', include(blogs_router.urls))
]


