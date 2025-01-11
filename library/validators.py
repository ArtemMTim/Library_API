from rest_framework import serializers

from library.models import Author


class AuthorValidator:
    """Валидатор автора."""

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        last_name = value["lact_name"]
        first_name = value["first_name"]
        patronymic = value["patronymic"]
        birth_date = value["birth_date"]
        death_date = value["death_date"]
        if Author.objects.filter(
            last_name=last_name,
            first_name=first_name,
            patronymic=patronymic,
        ).exists():
            raise serializers.ValidationError(
                "Такой автор уже существует в базе данных библиотеки."
            )
        if birth_date >= death_date:
            raise serializers.ValidationError(
                "Дата рождения не может быть больше или равна дате смерти."
            )
