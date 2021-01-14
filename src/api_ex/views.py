import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from .models import Post, Tag
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import redirect

from rest_framework.generics import CreateAPIView,ListAPIView,RetrieveAPIView,DestroyAPIView
from .forms import PostForm

from django.conf import settings

from .serializers import(
    PostListSerializer,
    PostDetailSerializer,
    TagListSerializer,
    TagDetailSerializer,
    PostCreateSerializer,
    TagCreateSerializer,
    TagDestroySerializer,
    PostDestroySerializer
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


class TagCreateView(CreateAPIView):
    serializer_class = TagCreateSerializer


class TagDeleteView(DestroyAPIView):
    serializer_class = TagDestroySerializer
    lookup_field = 'pk'
    lookup_url_kwarg = 'tag_id'
    queryset = Tag.objects.all()

class PostDeleteView(DestroyAPIView):
    serializer_class = PostDestroySerializer
    lookup_field = 'pk'
    lookup_url_kwarg = 'post_id'
    queryset = Post.objects.all()

# class UpdateName(generics.UpdateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostListSerializer
#     permission_classes = (permissions.IsAuthenticated,)

def post_view(request):
    posts = Post.objects.all().order_by("-id")
    return render(request, "post.html", context = {"posts":posts})  

def tag_view(request):
    tags = Tag.objects.all().order_by("-id")
    return render(request, "tag.html", context = {"tags":tags})  


def post_detail_view(request,post_id):
    post = Post.objects.get(id = post_id)
    return render(request, "post_detail.html", context = {"post":post})  

def tag_detail_view(request, tag_id):
    posts = Post.objects.filter(tags__id = tag_id)
    return render(request, "post_detail.html", context = {"posts":posts})  

def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return render(request, 'post.html')
    else:
        form = PostForm()
    return render(request, 'post_create.html', {'form': form})

# def deletePost(request,post_id):
#     Post.objects.filter(id = post_id).delete()
#     return JsonResponse(data = {"success":True} )

# def deleteTag(request,tag_id):
#     Tag.objects.filter(id = tag_id).delete()
#     return JsonResponse(data = {"success":True} )

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