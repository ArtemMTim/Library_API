from django.db import models

class Author(models.Model):
    pass
    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.patronymic}"

class Book(models.Model):
    pass
    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"

    def __str__(self):
        return self.title

# Create your models here.
