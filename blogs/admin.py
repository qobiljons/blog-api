from django.db.models.aggregates import Count
from django.contrib import admin
from django.utils.html import format_html, urlencode
from django.urls import reverse
from . import models

# Register your models here.


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'get_blog_count']
    search_fields = ['title']

    @admin.display(ordering='blog_count')
    def get_blog_count(self, blog):
        url = (
            reverse('admin:blogs_blog_changelist')
            + '?'
            + urlencode({
                'blog__id': str(blog.id)
            }))
        return format_html('<a href="{}">{} Blogs</a>', url, blog.blog_count)


    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(blog_count=Count('blogs'))
        return queryset
    

    
    




@admin.register(models.Blog)
class BlogAdmin(admin.ModelAdmin):
    pass



@admin.register(models.Review)
class ReviewAdmin(admin.ModelAdmin):
    pass

