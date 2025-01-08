from django.shortcuts import render
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    get_object_or_404,
)

from library.models import Author, Book
from library.serializers import AuthorSerializer, BookSerializer


class AuthorListApiView(ListAPIView):
    """Контроллер списка авторов."""

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorRetrieveApiView(RetrieveAPIView):
    """Контроллер просмотра автора."""

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorUpdateApiView(UpdateAPIView):
    """Контроллер изменения автора."""

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorDestroyApiView(DestroyAPIView):
    """Контроллер удаления автора."""

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorCreateApiView(CreateAPIView):
    """Контроллер создания автора."""

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookListApiView(ListAPIView):
    """Контроллер списка книг."""

    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookRetrieveApiView(RetrieveAPIView):
    """Контроллер просмотра книги."""

    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookUpdateApiView(UpdateAPIView):
    """Контроллер изменения книги."""

    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDestroyApiView(DestroyAPIView):
    """Контроллер удаления книги."""

    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookCreateApiView(CreateAPIView):
    """Контроллер создания книги."""

    queryset = Book.objects.all()
    serializer_class = BookSerializer


# Create your views here.
