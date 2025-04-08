from rest_framework import serializers
from .models import Post, Comment, Like


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'user_id', 'content', 'created_at')


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ('id', 'user_id', 'created_at')


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    likes_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ('id', 'user_id', 'title', 'content', 'post_type',
                  'image', 'created_at', 'updated_at', 'comments', 'likes_count')

    def get_likes_count(self, obj):
        return obj.likes.count()