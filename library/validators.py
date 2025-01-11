from rest_framework import serializers

from library.models import Author


class AuthorValidator:
    """Валидатор автора."""

    def __init__(self, field):
        self.field = field

    def __call__(self, value):

        if "last_name" in value and "first_name" in value and "patronymic" in value:
            # случай с автором с полным ФИО
            last_name = value["last_name"]
            first_name = value["first_name"]
            patronymic = value["patronymic"]
            if Author.objects.filter(
                last_name=last_name,
                first_name=first_name,
                patronymic=patronymic,
            ).exists():
                raise serializers.ValidationError(
                    "Такой автор уже существует в базе данных библиотеки."
                )
        if "last_name" in value and "first_name" in value:
            # случай с автором с неполным ФИО - только имя и фамилия
            last_name = value["last_name"]
            first_name = value["first_name"]
            patronymic = None
            if Author.objects.filter(
                last_name=last_name,
                first_name=first_name,
                patronymic=patronymic,
            ).exists():
                raise serializers.ValidationError(
                    "Такой автор уже существует в базе данных библиотеки."
                )
        if "birth_date" in value and "death_date" in value:
            # случай с автором с датами рождения и смерти
            birth_date = value["birth_date"]
            death_date = value["death_date"]
            if birth_date >= death_date:
                raise serializers.ValidationError(
                    "Дата рождения не может быть больше или равна дате смерти."
                )
