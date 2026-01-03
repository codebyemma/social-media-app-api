from rest_framework import serializers
from posts.models import Comment
from users.serializers import UserProfileSerializer


class CommentSerializer(serializers.ModelSerializer):
    user = UserProfileSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ["id", "text", "user", "created_at"]
