from django.urls import path,include
from .views import home,all_posts,post_details

urlpatterns = [
    # path('', home),
    path('posts/',all_posts),
    path('posts/<int:post_id>/',post_details),
    
]