from django.urls import path
from .views import CreditCardView, CreditCardDetailView


urlpatterns = [
    path("credit-card/", CreditCardView.as_view()),
    path("credit-card/<pk>/", CreditCardDetailView.as_view()),
]
