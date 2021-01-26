from django.urls import path,include
from .views import (
    home,
    post_view,
    tag_view,
    post_detail_view,
    tag_detail_view,
    post_create,
    tag_create,
    PostListView,
    PostDetailView,
    TagListView,
    TagDetailView, 
    PostCreateView,
    TagCreateView,
    PostDeleteView,
    TagDeleteView,
    # deletePost,
    # deleteTag
)

app_name = 'api_ex'

urlpatterns = [
    # path('home/', home, name='home'),
    path('', post_view, name='post_list'),
    path('tag.view/', tag_view, name='tag_list'),
    path('post.view/<int:post_id>/', post_detail_view, name='post_details'),
    path('tag.view/<int:tag_id>/', tag_detail_view, name = 'tag_details'),
    path('post.create/',post_create, name='post_create'),
    path('tag.create/',tag_create, name='tag_create'),
    
    path('api.posts/',PostListView.as_view()),
    path('api.posts/<int:post_id>/',PostDetailView.as_view()),
    path('api.post/create', PostCreateView.as_view()),
    path('api.tags/',TagListView.as_view()),
    path('api.tags/<int:tag_id>/',TagDetailView.as_view()),
    path('api.tag/create', TagCreateView.as_view()),
    path('api.post/delete/<int:post_id>/', PostDeleteView.as_view()),
    path('api.tag/delete/<int:tag_id>/',  TagDeleteView.as_view()),
    

    # path('posts/',PostListView.as_view()),
    # path('posts/<int:post_id>/',PostDetailView.as_view()),
    # path('post/create', PostCreateView.as_view()),
    # path('tags/',TagListView.as_view()),
    # path('tags/<int:tag_id>/',TagDetailView.as_view()),
    # path('tag/create', TagCreateView.as_view()),
    # path('post/delete/<int:post_id>/', PostDeleteView.as_view()),
    # path('tag/delete/<int:tag_id>/',  TagDeleteView.as_view()),
    
]



 # path('post/delete/<int:post_id>/', deletePost),
    # path('tag/delete/<int:tag_id>/', deleteTag),