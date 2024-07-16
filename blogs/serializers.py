from rest_framework import serializers
from . import models

class BlogSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=200)
    author = serializers.CharField(max_length=200)
    body = serializers.CharField(max_length=2000)
    category = serializers.CharField(max_length=255)
