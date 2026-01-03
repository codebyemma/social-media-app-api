from django.urls import path
from .views import (
    PostCreateView,
    FeedView,
    LikePostView,
    UnlikePostView,
    CommentCreateView,
    PostDetailView,
    CommentDeleteView,
)

urlpatterns = [
    path("create/", PostCreateView.as_view()),
    path("feed/", FeedView.as_view()),
    path("like/<int:post_id>/", LikePostView.as_view()),
    path("unlike/<int:post_id>/", UnlikePostView.as_view()),
    path("comment/<int:post_id>/", CommentCreateView.as_view()),
    path("post/<int:pk>/", PostDetailView.as_view()),
    path("comment/delete/<int:pk>/", CommentDeleteView.as_view()),
]
