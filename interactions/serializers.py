from rest_framework import serializers
from interactions.models import Comment
from users.serializers import UserProfileSerializer


class CommentSerializer(serializers.ModelSerializer):
    user = UserProfileSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ["id", "text", "user", "created_at"]
