from django.db import models
from django.conf import settings

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=255)
    def __str__(self):
        return self.title


class Blog(models.Model):
    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'blogs'
        verbose_name = 'blog'
    CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
    ]
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published = models.CharField(max_length=10 ,choices=CHOICES, default='draft')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="blogs")
    
    def __str__(self):
        return self.title
    

class Review(models.Model):
    CHOICES = [
        ('1', '⭐'),
        ('2', '⭐⭐'),
        ('3', '⭐⭐⭐'),
        ('4', '⭐⭐⭐⭐'),
        ('5', '⭐⭐⭐⭐⭐'),
    ]
    rating = models.IntegerField(choices=CHOICES, default=3)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="reviews")
    date = models.DateField(auto_now_add=True)
    comment = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="reviews")
    def __str__(self):
        return f"{self.blog.title}: Rating: {self.get_rating_display()}"

