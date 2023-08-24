# Generated by Django 4.2.4 on 2023-08-24 13:39

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("creditcards", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="CardPurchase",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=127)),
                ("purchaseInstallments", models.IntegerField()),
                ("value", models.CharField(max_length=127)),
                ("category", models.CharField(max_length=127)),
                ("purchaseDate", models.DateField()),
                (
                    "creditCard",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="cardPurchases",
                        to="creditcards.creditcard",
                    ),
                ),
            ],
        ),
    ]