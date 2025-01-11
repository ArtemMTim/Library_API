from rest_framework.serializers import ModelSerializer, SerializerMethodField

from library.models import Author, Book
from library.validators import AuthorValidator


class AuthorSerializer(ModelSerializer):
    """Сериализатор автора."""

    authors_books = SerializerMethodField()

    def get_authors_books(self, author):
        return [book.title for book in author.book_set.all()]

    class Meta:
        model = Author
        validators = [AuthorValidator(field="__all__")]
        fields = (
            "id",
            "last_name",
            "first_name",
            "patronymic",
            "birth_date",
            "death_date",
            "authors_books",
        )


class BookSerializer(ModelSerializer):
    """Сериализатор книги."""

    class Meta:
        model = Book
        fields = "__all__"
