from rest_framework import generics, permissions, status
from .models import Post, Like, Comment
from .serializers import (
    PostSerializer,
    PostCreateSerializer,
    CommentCreateSerializer,
)
from interactions.models import Follow
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .permissions import IsOwner, IsCommentOwner

class PostCreateView(generics.CreateAPIView):
    serializer_class = PostCreateSerializer
    permission_classes = [permissions.IsAuthenticated]


class FeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        following_ids = Follow.objects.filter(
            follower=user
        ).values_list("following_id", flat=True)

        return Post.objects.filter(
            user__in=list(following_ids) + [user.id]
        ).order_by("-created_at")

class LikePostView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)

        like, created = Like.objects.get_or_create(
            user=request.user,
            post=post,
        )

        if not created:
            return Response(
                {"detail": "Already liked"},
                status=status.HTTP_200_OK,
            )

        return Response(
            {"detail": "Post liked"},
            status=status.HTTP_201_CREATED,
        )


class UnlikePostView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)

        deleted, _ = Like.objects.filter(
            user=request.user,
            post=post,
        ).delete()

        if deleted == 0:
            return Response(
                {"detail": "You have not liked this post"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        return Response(
            {"detail": "Post unliked"},
            status=status.HTTP_200_OK,
        )

class CommentCreateView(generics.CreateAPIView):
    serializer_class = CommentCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["post_id"] = self.kwargs["post_id"]
        return context


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [
        permissions.IsAuthenticated,
        IsOwner,
    ]

class CommentDeleteView(generics.DestroyAPIView):
    queryset = Comment.objects.all()
    permission_classes = [
        permissions.IsAuthenticated,
        IsCommentOwner,
    ]
