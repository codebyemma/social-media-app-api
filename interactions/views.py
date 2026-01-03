from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from .models import Follow

User = get_user_model()

class FollowUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        target_user = get_object_or_404(User, id=user_id)

        if request.user == target_user:
            return Response(
                {"detail": "You cannot follow yourself"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        follow, created = Follow.objects.get_or_create(
            follower=request.user,
            following=target_user,
        )

        if not created:
            return Response(
                {"detail": "Already following"},
                status=status.HTTP_200_OK,
            )

        return Response(
            {"detail": "Followed successfully"},
            status=status.HTTP_201_CREATED,
        )
class UnfollowUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, user_id):
        target_user = get_object_or_404(User, id=user_id)

        deleted, _ = Follow.objects.filter(
            follower=request.user,
            following=target_user,
        ).delete()

        if deleted == 0:
            return Response(
                {"detail": "You are not following this user"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        return Response(
            {"detail": "Unfollowed successfully"},
            status=status.HTTP_200_OK,
        )
