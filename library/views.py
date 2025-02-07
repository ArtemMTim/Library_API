import textwrap
from datetime import date, datetime, timedelta

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView, get_object_or_404)
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from library.models import Author, Book
from library.pagination import PageSize
from library.serializers import AuthorSerializer, BookSerializer
from library.tasks import email_notification, telegram_notification
from users.models import User


class AuthorListApiView(ListAPIView):
    """Контроллер списка авторов."""

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = PageSize
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filterset_fields = ("last_name", "first_name", "patronymic")
    ordering_fields = ("last_name", "first_name", "patronymic", "birth_date")


class AuthorRetrieveApiView(RetrieveAPIView):
    """Контроллер просмотра автора."""

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticated]


class AuthorUpdateApiView(UpdateAPIView):
    """Контроллер изменения автора."""

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class AuthorDestroyApiView(DestroyAPIView):
    """Контроллер удаления автора."""

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class AuthorCreateApiView(CreateAPIView):
    """Контроллер создания автора."""

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class BookListApiView(ListAPIView):
    """Контроллер списка книг."""

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = PageSize
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filterset_fields = (
        "title",
        "author",
        "genre",
        "publication_year",
        "publishing",
        "book_year",
        "isbn",
        "issue",
        "issue_date",
        "reader",
    )
    ordering_fields = ("title", "author", "genre", "isbn")


class BookRetrieveApiView(RetrieveAPIView):
    """Контроллер просмотра книги."""

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


class BookUpdateApiView(UpdateAPIView):
    """Контроллер изменения книги."""

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class BookDestroyApiView(DestroyAPIView):
    """Контроллер удаления книги."""

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class BookCreateApiView(CreateAPIView):
    """Контроллер создания книги."""

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class IssueBookApiView(APIView):
    """Контроллер выдачи книги."""

    permission_classes = [IsAuthenticated, IsAdminUser]

    def post(self, *args, **kwargs):
        user_id = self.request.data.get("user")
        book_id = self.request.data.get("book")
        if Book.objects.filter(reader=user_id, id=book_id, issue=True).exists():
            book = get_object_or_404(Book, id=book_id)
            user = get_object_or_404(User, id=user_id)
            book.reader = None
            book.issue_date = None
            book.return_date = None
            book.issue = False
            book.save()
            # формируем сообщение и тему письма о возврате книги,
            # отправляем отложенной функцией через почту либо телеграм (при наличии у читателя)
            message = textwrap.dedent(
                f"""\
            Здравствуйте!
            Вы вернули книгу "{book.title}" автора {book.author}. Спасибо!
            С Уважением, администрация библиотеки!
            """
            )
            subject = "Возврат книги"
            email_notification.delay(email=user.email, subject=subject, message=message)
            if user.tg_id:
                telegram_notification.delay(chat_id=user.tg_id, message=message)

            return Response({"message": "Книга возвращена"})
        else:
            book = get_object_or_404(Book, id=book_id)
            user = get_object_or_404(User, id=user_id)
            book.reader = user
            book.issue_date = date.today()
            book.return_date = book.issue_date + timedelta(days=30)
            book.issue = True
            book.save()
            # формируем сообщение и тему письма о выдаче книги,
            # отправляем отложенной функцией через почту либо телеграм (при наличии у читателя)
            message = textwrap.dedent(
                f"""\
            Здравствуйте!
            Вам выдали книгу "{book.title}" автора {book.author} на 30 календарных дней до {book.return_date}.
            Приятного чтения!
            С Уважением, администрация библиотеки!
            """
            )
            subject = "Выдача книги"
            email_notification.delay(email=user.email, subject=subject, message=message)
            if user.tg_id:
                telegram_notification.delay(chat_id=user.tg_id, message=message)
            return Response({"message": "Книга выдана"})


# Create your views here.
