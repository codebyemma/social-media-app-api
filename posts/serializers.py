from rest_framework import serializers
from .models import Post, Like
from accounts.serializers import UserProfileSerializer


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["content"]

    def create(self, validated_data):
        request = self.context["request"]
        post_id = self.context["post_id"]

        return Comment.objects.create(
            user=request.user,
            post_id=post_id,
            **validated_data
        )


class CommentSerializer(serializers.ModelSerializer):
    user = UserProfileSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ["id", "user", "content", "created_at"]


class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["content"]

    def create(self, validated_data):
        request = self.context["request"]
        return Post.objects.create(
            author=request.user,
            **validated_data
        )


class PostSerializer(serializers.ModelSerializer):
    author = UserProfileSerializer(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    likes_count = serializers.SerializerMethodField()
    is_liked = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            "id",
            "author",
            "content",
            "created_at",
            "likes_count",
            "is_liked",
        ]

    def get_likes_count(self, obj):
        return obj.likes.count()

    def get_is_liked(self, obj):
        request = self.context.get("request")
        if request is None or request.user.is_anonymous:
            return False
        return obj.likes.filter(user=request.user).exists()
