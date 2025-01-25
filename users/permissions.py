from rest_framework import permissions


class IsUser(permissions.BasePermission):
    """Проверка на пользователя. Применяетс для проверки доступа к странице пользователя,
    чтобы избежать доступа к чужим страницам."""

    def has_object_permission(self, request, view, obj):
        return obj.email == request.user.email
