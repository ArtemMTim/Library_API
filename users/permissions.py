from rest_framework import permissions


class IsUser(permissions.BasePermission):
    """Проверка на пользователя."""

    def has_object_permission(self, request, view, obj):
        return obj.email == request.user.email
