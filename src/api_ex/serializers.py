from rest_framework import serializers
from .models import Tag, Post

class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        exclude = ('body',)

class PostDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        exclude = ('id',)