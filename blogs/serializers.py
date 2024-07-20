from rest_framework import serializers
from .models import Category, Author, Blog, Review


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'age', 'blogs_count', 'user_id']
    blogs_count = serializers.IntegerField(read_only=True)
    user_id = serializers.IntegerField(read_only=True)

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ["id", "rating", "date", "comment", "author", "blog"]
    blog = serializers.PrimaryKeyRelatedField(read_only = True)  
    def create(self, validated_data):
        blog_id = self.context["blog_id"]
        author = self.context["author"]
        return Review.objects.create(blog_id=blog_id, author=author, **validated_data)
    

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'title', 'author_id', 'body', 'category', 'reviews', 'created_at']
    reviews = ReviewSerializer(many=True, read_only=True)
    def create(self, validated_data):
        author = self.context["author"]
        return Blog.objects.create(author=author, **validated_data)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model= Category
        fields = ["id", "title", "blogs_count"]
    blogs_count = serializers.IntegerField(read_only=True)

