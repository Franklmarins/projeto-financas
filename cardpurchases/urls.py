from django.urls import path
from .views import CardPurchaseView, CardPurchaseDetailView

urlpatterns = [
    path("purchase/<pk>/", CardPurchaseView.as_view()),
    path("purchase/update/<pk>/", CardPurchaseDetailView.as_view()),
]
