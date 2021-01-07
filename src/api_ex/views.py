import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Post, Tag
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView,ListAPIView,RetrieveAPIView

from .serializers import(
    PostListSerializer,
    PostDetailSerializer,
    TagListSerializer,
    TagDetailSerializer,
    PostCreateSerializer,
    TagCreateSerializer
    )

def home(request):
    return HttpResponse('<h1>Hello World</h1>')

class PostListView(ListAPIView):
    serializer_class = PostListSerializer
    queryset = Post.objects.all()

class TagListView(ListAPIView):
    serializer_class = TagListSerializer
    queryset = Tag.objects.all()

class PostDetailView(RetrieveAPIView):
    serializer_class = PostDetailSerializer
    queryset = Post.objects.all()
    lookup_field = 'pk' # id
    lookup_url_kwarg = 'post_id'

class TagDetailView(RetrieveAPIView):
    serializer_class = TagDetailSerializer
    queryset = Tag.objects.all()
    lookup_field = 'pk' # id
    lookup_url_kwarg = 'tag_id'

class PostCreateView(CreateAPIView):
    serializer_class = PostCreateSerializer

class TagCreateView(CreateAPIView):
    serializer_class = TagCreateSerializer



# @api_view(['GET'])
# def all_posts(request):
#     posts = Post.objects.all()
#     # posts = [{'title':i.title, 'body':i.body} for i in posts]
#     ser = PostListSerializer(posts , many = True)
    
#     return Response(data = ser.data)
# @api_view(['GET'])
# def all_tags(request):
#     tags = Tag.objects.all()
#     ser = TagListSerializer(tags , many = True)
    # return Response(data = ser.data)
# @api_view(['POST'])
# def post_create(request):
#     ser = PostCreateSerializer(data = request.data)
#     ser.is_valid(raise_exception=True)
#     Post.objects.create(**ser.data)
#     return Response(data = {"success":True,"message":"Post created"})


# @api_view(['POST'])
# def tag_create(request):
#     ser = TagCreateSerializer(data = request.data)
#     ser.is_valid(raise_exception=True)
#     Tag.objects.create(**ser.data)
#     return Response(data = {"success":True,"message":"Tag created"})

# @api_view(['GET'])
# def post_details(request, post_id):
#     posts = Post.objects.get(id = post_id)
#     ser = PostDetailSerializer(posts)
#     return Response(data = ser.data)


# @api_view(['GET'])
# def tag_details(request, tag_id):
#     tags = Tag.objects.get(id = tag_id)
#     ser = TagDetailSerializer(tags)
#     return Response(data = ser.data)