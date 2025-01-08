from django.contrib import admin
from .models import Author, Book


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "last_name",
        "first_name",
        "patronymic",
        "birth_date",
        "death_date",
        "image",
        "biography",
    )
    search_fields = (
        "last_name",
        "first_name",
        "patronymic",
        "birth_date",
        "death_date",
    )
    list_filter = (
        "last_name",
        "first_name",
        "patronymic",
        "birth_date",
        "death_date",
    )


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "description",
        "image",
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
    search_fields = (
        "title",
        "description",
        "author",
        "genre",
    )
    list_filter = (
        "title",
        "description",
        "author",
        "genre",
    )
