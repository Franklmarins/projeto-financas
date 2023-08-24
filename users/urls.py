from django.urls import path
from .views import UserView, UserDetailView

urlpatterns = [
    path('user/', UserView.as_view()),
    path('user/<pk>/', UserDetailView.as_view())
]