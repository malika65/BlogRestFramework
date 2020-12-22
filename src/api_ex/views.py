import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Post, Tag
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PostListSerializer,PostDetailSerializer

def home(request):
    return HttpResponse('<h1>Hello World</h1>')

@api_view(['GET'])
def all_posts(request):
    posts = Post.objects.all()
    # posts = [{'title':i.title, 'body':i.body} for i in posts]
    ser = PostListSerializer(posts , many = True)
    
    return Response(data = ser.data)


@api_view(['GET'])
def post_details(request, post_id):
    posts = Post.objects.get(id = post_id)
    ser = PostDetailSerializer(posts)
    return Response(data = ser.data)