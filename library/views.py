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
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorUpdateApiView(UpdateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorDestroyApiView(DestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorCreateApiView(CreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookListApiView(ListAPIView):
    """Контроллер списка книг."""

    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookRetrieveApiView(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookUpdateApiView(UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDestroyApiView(DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookCreateApiView(CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# Create your views here.
