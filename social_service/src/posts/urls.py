from django.urls import path
from .views import (
    PostListCreateAPIView,
    PostDetailAPIView,
    CommentListCreateAPIView,
    LikeCreateAPIView
)

urlpatterns = [
    path('posts/', PostListCreateAPIView.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', PostDetailAPIView.as_view(), name='post-detail'),
    path('posts/<int:post_id>/comments/', CommentListCreateAPIView.as_view(), name='comment-list-create'),
    path('posts/<int:post_id>/like/', LikeCreateAPIView.as_view(), name='post-like'),
]