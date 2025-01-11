from django.shortcuts import render
from datetime import datetime, date
from rest_framework.views import APIView
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
from users.models import User
from rest_framework.response import Response
from library.pagination import PageSize


class AuthorListApiView(ListAPIView):
    """Контроллер списка авторов."""

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    pagination_class = PageSize


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
    pagination_class = PageSize


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


class IssueBookApiView(APIView):
    """Контроллер выдачи книги."""

    def post(self, *args, **kwargs):
        user_id = self.request.data.get("user")
        book_id = self.request.data.get("book")
        if Book.objects.filter(reader=user_id, id=book_id, issue=True).exists():
            book = get_object_or_404(Book, id=book_id)
            book.reader = None
            book.issue_date = None
            book.issue = False
            book.save()
            return Response({"message": "Книга возвращена"})
        else:
            book = get_object_or_404(Book, id=book_id)
            user = get_object_or_404(User, id=user_id)
            book.reader = user
            book.issue_date = date.today()
            book.issue = True
            book.save()
            return Response({"message": "Книга выдана"})


# Create your views here.
