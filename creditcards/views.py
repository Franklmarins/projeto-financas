from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .permissions import IsProductOwner
from .models import CreditCard
from .serializers import creditCardSerializer
from rest_framework.response import Response


class CreditCardView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]

    queryset = CreditCard.objects.all()
    serializer_class = creditCardSerializer

    def get_queryset(self):
        return CreditCard.objects.filter(user_id=self.request.user.id)

    def perform_create(self, serializer):
        return serializer.save(user_id=self.request.user.id)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class CreditCardDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsProductOwner]

    queryset = CreditCard.objects.all()
    serializer_class = creditCardSerializer
