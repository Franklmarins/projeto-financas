from django.urls import path
from .views import UserView, UserDetailView
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path("user/", UserView.as_view()),
    path("user/<pk>/", UserDetailView.as_view()),
    path("login/", TokenObtainPairView.as_view()),
]
