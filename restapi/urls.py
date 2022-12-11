from django.urls import path
from .views import PostsView, postsdetail

urlpatterns = [
    path('posts/', PostsView),
    path('posts/<int:pk>', postsdetail)
]