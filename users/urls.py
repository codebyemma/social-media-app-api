from django.urls import path
from .views import RegisterView

urlpatterns = [
    path("register/", RegisterView.as_view()),
    path("profile/<int:pk>/", UserProfileView.as_view()),

]
