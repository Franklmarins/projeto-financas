from rest_framework import permissions
from .models import CreditCard
from rest_framework.views import View


class IsProductOwner(permissions.BasePermission):
    def has_object_permission(self, request, view: View, obj: CreditCard):
        return request.user.is_authenticated and obj.user == request.user
