from rest_framework import serializers
from .models import CardPurchase


class cardPurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CardPurchase
        fields = [
            "id",
            "name",
            "purchaseInstallments",
            "value",
            "category",
            "purchaseDate",
            "creditCard_id",
        ]
        read_only_fields = ["creditCard_id"]
