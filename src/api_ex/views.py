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
    return render(request, "post.html", context = {"posts":posts})  

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

