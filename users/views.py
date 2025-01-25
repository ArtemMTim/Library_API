from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView)
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser

from users.models import User
from users.serializers import UserSerializer
from users.permissions import IsUser


class UserCreateApiView(CreateAPIView):
    """Контроллер создания пользователя."""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny,]

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class UserDeleteApiView(DestroyAPIView):
    """Контроллер удаления пользователя."""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsUser]


class UserUpdateApiView(UpdateAPIView):
    """Контроллер изменения пользователя."""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsUser]


class UserRetrieveApiView(RetrieveAPIView):
    """Контроллер просмотра пользователя."""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsUser]


class UserListApiView(ListAPIView):
    """Контроллер просмотра списка пользователей."""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
