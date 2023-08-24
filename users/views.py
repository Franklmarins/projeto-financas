from rest_framework.views import APIView,Response, Request
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from .models import User
from .serializers import UserSerializer

class UserView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
