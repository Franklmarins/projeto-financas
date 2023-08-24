from django.db import models
import uuid

class CreditCard(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=127)
    limit = models.IntegerField()
    invoiceDueDate = models.IntegerField()

    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="creditCards")