from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import IsAccountOwner
from rest_framework.views import APIView, Request, Response, status
from rest_framework.generics import (
    CreateAPIView,
    RetrieveUpdateDestroyAPIView,
    RetrieveAPIView,
)
from .models import User
from .serializers import UserSerializer
from django.shortcuts import get_object_or_404


class UserView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GetUserDetail(RetrieveAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        user = get_object_or_404(User, id=request.user.id)
        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)


class UserDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]

    queryset = User.objects.all()
    serializer_class = UserSerializer
