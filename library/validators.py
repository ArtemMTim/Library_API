from rest_framework import serializers

from library.models import Author


class AuthorValidator:
    """Валидатор автора."""

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        last_name = value.get("last_name", None)
        first_name = value.get("first_name", None)
        patronymic = value.get("patronymic", None)
        birth_date = value.get("birth_date", None)
        death_date = value.get("death_date", None)
        if Author.objects.filter(
            last_name=last_name,
            first_name=first_name,
            patronymic=patronymic,
        ).exists():
            raise serializers.ValidationError(
                "Такой автор уже существует в базе данных библиотеки."
            )

        if birth_date and death_date:
            # случай с автором с датами рождения и смерти
            # birth_date = value["birth_date"]
            # death_date = value["death_date"]
            if birth_date >= death_date:
                raise serializers.ValidationError(
                    "Дата рождения не может быть больше или равна дате смерти."
                )
