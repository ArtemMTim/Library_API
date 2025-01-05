from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Модель пользователя сервиса библиотеки."""

    username = None
    email = models.EmailField(unique=True, verbose_name="Электронная почта")
    first_name = models.CharField(
        max_length=50,
        verbose_name="Имя",
        blank=True,
        null=True,
        help_text="Введите Ваше имя",
    )
    last_name = models.CharField(
        max_length=50,
        verbose_name="Фамилия",
        blank=True,
        null=True,
        help_text="Введите Вашу фамилию",
    )
    patronymic = models.CharField(
        max_length=50,
        verbose_name="Отчество",
        blank=True,
        null=True,
        help_text="Введите Ваше отчество",
    )
    phone_number = models.CharField(
        max_length=35,
        verbose_name="Номер телефона",
        blank=True,
        null=True,
        help_text="Введите номер телефона",
    )
    address = models.CharField(
        max_length=400,
        verbose_name="Адрес",
        blank=True,
        null=True,
        help_text="Введите Ваш адрес",
    )
    avatar = models.ImageField(
        upload_to="users/avatars",
        verbose_name="Аватар",
        blank=True,
        null=True,
        help_text="Загрузите Ваш аватар",
    )
    birth_date = models.DateField(
        verbose_name="Дата рождения",
        blank=True,
        null=True,
        help_text="Введите Вашу дату рождения",
    )
    tg_id = models.CharField(
        max_length=255,
        verbose_name="ID профиля Telegram",
        blank=True,
        null=True,
        help_text="Введите ID Вашего профиля Telegram",
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь сервиса библиотеки"
        verbose_name_plural = "Пользователи сервиса библиотеки"

    def __str__(self):
        return self.email
