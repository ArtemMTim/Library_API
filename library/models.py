from django.db import models

class Author(models.Model):
    """Модель автора."""
    last_name = models.CharField(
        max_length=50,
        verbose_name="Фамилия",
        blank=True,
        null=True,
        help_text="Введите фамилию автора",
    )
    first_name = models.CharField(
        max_length=50,
        verbose_name="Имя",
        blank=True,
        null=True,
        help_text="Введите имя автора",
    )
    patronymic = models.CharField(
        max_length=50,
        verbose_name="Отчество",
        blank=True,
        null=True,
        help_text="Введите отчество автора",
    )
    birth_date = models.DateField(
        verbose_name="Дата рождения автора",
        blank=True,
        null=True,
        help_text="Введите дату рождения автора",
    )
    death_date = models.DateField(
        verbose_name="Дата смерти автора",
        blank=True,
        null=True,
        help_text="Введите дату смерти автора",
    )
    image = models.ImageField(
        upload_to="users/authors_foto",
        verbose_name="Изображение автора",
        blank=True,
        null=True,
        help_text="Загрузите изображение автора",
    )
    biography = models.TextField(
        verbose_name="Краткая бтография",
        blank=True,
        null=True,
        help_text="Введите краткую биографию автора",
    )

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.patronymic}"

class Book(models.Model):
    """Модель книги."""
    pass
    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"

    def __str__(self):
        return self.title

# Create your models here.
