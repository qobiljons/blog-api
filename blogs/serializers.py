from rest_framework import serializers
from .models import Category, Author, Blog, Review



class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'age', 'blogs_count', 'user']
    blogs_count = serializers.IntegerField(read_only=True)
        
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ["id", "rating", "date", "comment", "author"]
    
class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'title', 'author', 'body', 'category', 'reviews', 'created_at']
    reviews = ReviewSerializer(many=True, read_only=True)

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model= Category
        fields = ["id", "title", "blogs_count"]
    blogs_count = serializers.IntegerField(read_only=True)



