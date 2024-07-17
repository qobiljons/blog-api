from django.db.models.aggregates import Count
from django.contrib import admin
from django.utils.html import format_html, urlencode
from django.urls import reverse
from . import models


# Register your models here.

class AgeFilter(admin.SimpleListFilter):
    title = ('age')
    parameter_name = 'age'

    def lookups(self, request, model_admin):
        return [
            ('<16', ('Minor')),
            ('16-19', ('Teenager')),
            ('20-29', ('Young Adult')),
            ('30-39', ('Adult')),
            ('>=40', ('Senior')),
        ]

    def queryset(self, request, queryset):
        if self.value() == '<16':
            return queryset.filter(age__lt=16)
        elif self.value() == '16-19':
            return queryset.filter(age__gte=16, age__lt=20)
        elif self.value() == '20-29':
            return queryset.filter(age__gte=20, age__lt=30)
        elif self.value() == '30-39':
            return queryset.filter(age__gte=30, age__lt=40)
        elif self.value() == '>=40':
            return queryset.filter(age__gte=40)
        return queryset

@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'user',  'age', "first_name", "last_name", "get_blog_count"]
    search_fields = ['user__first_name', 'user__last_name']
    list_filter = [AgeFilter]

    list_select_related = ['user']

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
    search_fields = ["title", "category", "author"]
    autocomplete_fields = ['category']
    list_display = ['title', 'author', 'category', 'created_at', 'updated_at', 'published']
    list_per_page = 10
    prepopulated_fields = {
        'slug': ['title']
    }
    list_filter = ['category', 'updated_at', 'created_at', 'published']


@admin.register(models.Review)
class ReviewAdmin(admin.ModelAdmin):
    search_fields = ['blog__title', 'author__username', 'date'] 
    autocomplete_fields = ['blog', 'author']
    list_display = ['blog', 'author', 'rating', 'date']
    list_filter = ['rating', 'date', 'author']
    ordering = ['author']  