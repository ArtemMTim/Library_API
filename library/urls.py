from django.urls import path
from rest_framework.permissions import AllowAny


from library.apps import LibraryConfig

# from users.views import UserCreateApiView, UserDeleteApiView, UserListApiView, UserRetrieveApiView, UserUpdateApiView

app_name = LibraryConfig.name

urlpatterns = []
