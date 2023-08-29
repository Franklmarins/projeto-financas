from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import cardPurchaseSerializer
from .models import CardPurchase
from rest_framework.response import Response


class CardPurchaseView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]

    queryset = CardPurchase.objects.all()
    serializer_class = cardPurchaseSerializer

    def get_queryset(self):
        return CardPurchase.objects.filter(creditCard_id=self.kwargs["pk"])

    def perform_create(self, serializer):
        return serializer.save(creditCard_id=self.kwargs["pk"])

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class CardPurchaseDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]

    queryset = CardPurchase.objects.all()
    serializer_class = cardPurchaseSerializer
