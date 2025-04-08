from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.core.cache import cache
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer, LikeSerializer


class PostListCreateAPIView(APIView):
    def get(self, request):
        cache_key = 'all_posts'
        posts_data = cache.get(cache_key)

        if not posts_data:
            posts = Post.objects.all().order_by('-created_at')
            serializer = PostSerializer(posts, many=True)
            posts_data = serializer.data
            cache.set(cache_key, posts_data, 300)

        return Response(posts_data)

    def post(self, request):
        user_id = request.user.id if hasattr(request, 'user') and request.user.is_authenticated else request.data.get(
            'user_id')

        data = {**request.data, 'user_id': user_id}
        serializer = PostSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            cache.delete('all_posts')
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostDetailAPIView(APIView):
    def get(self, request, pk):
        cache_key = f'post_{pk}'
        post_data = cache.get(cache_key)

        if not post_data:
            try:
                post = Post.objects.get(pk=pk)
                serializer = PostSerializer(post)
                post_data = serializer.data
                cache.set(cache_key, post_data, 300)
            except Post.DoesNotExist:
                return Response({'error': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)

        return Response(post_data)

    def put(self, request, pk):
        try:
            post = Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return Response({'error': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)

        if post.user_id != request.user.id:
            return Response({'error': 'You do not have permission to edit this post'},
                            status=status.HTTP_403_FORBIDDEN)

        serializer = PostSerializer(post, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            cache.delete(f'post_{pk}')
            cache.delete('all_posts')
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            post = Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return Response({'error': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)

        if post.user_id != request.user.id:
            return Response({'error': 'You do not have permission to delete this post'},
                            status=status.HTTP_403_FORBIDDEN)

        post.delete()
        cache.delete(f'post_{pk}')
        cache.delete('all_posts')
        return Response(status=status.HTTP_204_NO_CONTENT)


class CommentListCreateAPIView(APIView):
    def post(self, request, post_id):
        try:
            post = Post.objects.get(pk=post_id)
        except Post.DoesNotExist:
            return Response({'error': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)

        user_id = request.user.id if hasattr(request, 'user') and request.user.is_authenticated else request.data.get(
            'user_id')

        data = {
            'post': post.id,
            'user_id': user_id,
            'content': request.data.get('content')
        }

        serializer = CommentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            cache.delete(f'post_{post_id}')
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LikeCreateAPIView(APIView):
    def post(self, request, post_id):
        try:
            post = Post.objects.get(pk=post_id)
        except Post.DoesNotExist:
            return Response({'error': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)

        user_id = request.user.id if hasattr(request, 'user') and request.user.is_authenticated else request.data.get(
            'user_id')

        like, created = Like.objects.get_or_create(post=post, user_id=user_id)

        if not created:
            like.delete()
            cache.delete(f'post_{post_id}')
            return Response({'status': 'unliked'}, status=status.HTTP_200_OK)

        cache.delete(f'post_{post_id}')
        return Response({'status': 'liked'}, status=status.HTTP_201_CREATED)
