from django.db import models

from users.models import User


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
        verbose_name="Краткая биография",
        blank=True,
        null=True,
        help_text="Введите краткую биографию автора",
    )

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"

    def __str__(self):
        return f"{self.last_name} {self.first_name}"


class Book(models.Model):
    """Модель книги."""

    title = models.CharField(
        max_length=255, verbose_name="Название", help_text="Введите название книги."
    )
    description = models.TextField(
        verbose_name="Описание книги",
        help_text="Введите описание книги",
        blank=True,
        null=True,
    )
    image = models.ImageField(
        upload_to="users/books_img",
        verbose_name="Обложка",
        blank=True,
        null=True,
        help_text="Загрузите обложку",
    )
    author = models.ManyToManyField(
        Author,
        verbose_name="Автор/авторы",
        help_text="Выберите автора/авторов",
    )
    genre = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="Жанр книги",
        help_text="Введите жанр книги.",
    )
    publication_year = models.IntegerField(
        verbose_name="Год публикации произведения",
        help_text="Введите год публикации произведения",
        blank=True,
        null=True,
    )
    publishing = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="Издательство",
        help_text="Введите название издательства.",
    )
    book_year = models.IntegerField(
        verbose_name="Год выпуска книги",
        help_text="Введите год выпуска книги",
        blank=True,
        null=True,
    )
    isbn = models.CharField(
        max_length=13,
        verbose_name="ISBN",
        help_text="Введите ISBN книги.",
        blank=True,
        null=True,
    )
    issue = models.BooleanField(
        default=False,
        verbose_name="Признак выдачи книги читателю",
        help_text="Введите признак выдачи книги читателю.",
    )
    issue_date = models.DateField(
        verbose_name="Дата выдачи книги читателю",
        blank=True,
        null=True,
        help_text="Введите дату выдачи книги читателю",
    )
    return_date = models.DateField(
        verbose_name="Дата возврата книги читателем",
        blank=True,
        null=True,
        help_text="Введите дату возврата книги читателем",
    )
    reader = models.ForeignKey(
        User,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name="Читатель",
        help_text="Укажите читателя.",
    )

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"

    def __str__(self):
        return self.title


# Create your models here.
