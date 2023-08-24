from django.db import models
import uuid

class CardPurchase(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=127)
    purchaseInstallments = models.IntegerField()
    value = models.CharField(max_length=127)
    category = models.CharField(max_length=127)
    purchaseDate = models.DateField()

    creditCard = models.ForeignKey("creditcards.CreditCard", on_delete=models.CASCADE, related_name="cardPurchases")
