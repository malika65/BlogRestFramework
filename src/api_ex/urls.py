from django.urls import path,include
from .views import (
    home,
    PostListView,
    PostDetailView,
    TagListView,
    TagDetailView, 
    PostCreateView,
    TagCreateView)

urlpatterns = [
    # path('', home),
    path('posts/',PostListView.as_view()),
    path('posts/<int:post_id>/',PostDetailView.as_view()),
    path('post/create', PostCreateView.as_view()),
    path('tags/',TagListView.as_view()),
    path('tags/<int:tag_id>/',TagDetailView.as_view()),
    path('tag/create', TagCreateView.as_view()),
    
]