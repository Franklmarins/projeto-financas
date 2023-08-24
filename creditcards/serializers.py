from rest_framework import serializers
from .models import CreditCard


class creditCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditCard
        fields = ["id", "name", "limit", "invoiceDueDate", "user_id"]
        read_only_fields = ["user_id"]
