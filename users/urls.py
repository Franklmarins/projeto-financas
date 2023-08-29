from django.urls import path
from .views import UserView, UserDetailView, GetUserDetail
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path("", UserView.as_view()),
    path("profile/", GetUserDetail.as_view()),
    path("profile/<pk>/", UserDetailView.as_view()),
    path("login/", TokenObtainPairView.as_view()),
]
