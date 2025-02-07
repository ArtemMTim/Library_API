from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from users.models import User


class UserSerializer(ModelSerializer):
    """Сериализатор пользователя."""

    reading_books = SerializerMethodField()

    def get_reading_books(self, user):
        return [f"'{book.title}' {book.author} до {book.return_date}" for book in user.book_set.all()]

    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "first_name",
            "last_name",
            "patronymic",
            "phone_number",
            "address",
            "birth_date",
            "tg_id",
            "reading_books",
        )
