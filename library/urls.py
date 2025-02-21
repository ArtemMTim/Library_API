from django.urls import path

from library.apps import LibraryConfig
from library.views import (AuthorCreateApiView, AuthorDestroyApiView,
                           AuthorListApiView, AuthorRetrieveApiView,
                           AuthorUpdateApiView, BookCreateApiView,
                           BookDestroyApiView, BookListApiView,
                           BookRetrieveApiView, BookUpdateApiView,
                           IssueBookApiView)

app_name = LibraryConfig.name

urlpatterns = [
    path("authors/", AuthorListApiView.as_view(), name="authors"),
    path("authors/<int:pk>/", AuthorRetrieveApiView.as_view(), name="authors_retrieve"),
    path(
        "authors/<int:pk>/update/", AuthorUpdateApiView.as_view(), name="authors_update"
    ),
    path(
        "authors/<int:pk>/delete/",
        AuthorDestroyApiView.as_view(),
        name="authors_delete",
    ),
    path("authors/create/", AuthorCreateApiView.as_view(), name="authors_create"),
    path("books/", BookListApiView.as_view(), name="books"),
    path("books/<int:pk>/", BookRetrieveApiView.as_view(), name="books_retrieve"),
    path("books/<int:pk>/update/", BookUpdateApiView.as_view(), name="books_update"),
    path("books/<int:pk>/delete/", BookDestroyApiView.as_view(), name="books_delete"),
    path("books/create/", BookCreateApiView.as_view(), name="books_create"),
    path("book_issue/", IssueBookApiView.as_view(), name="book_issue"),
]
