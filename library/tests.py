from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from library.models import Author, Book
from users.models import User


class AuthorTestCase(APITestCase):
    """Тесты для модели авторов."""

    def setUp(self):
        self.user = User.objects.create(email="test@test.com", is_staff=True)
        self.author = Author.objects.create(
            last_name="Test", first_name="Test", patronymic="Test"
        )
        self.client.force_authenticate(user=self.user)

    def test_author_retrieve(self):
        """Тест подробного просмотра автора."""
        url = reverse("library:authors_retrieve", args=(self.author.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        result = response.json().get("last_name")
        self.assertEqual(result, self.author.last_name)

    def test_author_create(self):
        """Тест создания автора."""
        data = {"last_name": "Test_new", "first_name": "Test", "patronymic": "Test"}
        url = reverse("library:authors_create")
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Author.objects.all().count(), 2)

    def test_author_create_already_exist(self):
        """Тест создания автора."""
        data = {"last_name": "Test", "first_name": "Test", "patronymic": "Test"}
        url = reverse("library:authors_create")
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.json().get("non_field_errors"),
            ["Такой автор уже существует в базе данных библиотеки."],
        )

    def test_author_create_wrong_date(self):
        """Тест создания автора."""
        data = {
            "last_name": "Test_new",
            "first_name": "Test_new",
            "patronymic": "Test_new",
            "birth_date": "2025-01-01",
            "death_date": "2024-10-01",
        }
        url = reverse("library:authors_create")
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.json().get("non_field_errors"),
            ["Дата рождения не может быть больше или равна дате смерти."],
        )

    def test_author_update(self):
        """Тест изменения автора."""
        data = {
            "last_name": "New_test",
            "first_name": "New_test",
            "patronymic": "New_test",
        }
        url = reverse("library:authors_update", args=(self.author.id,))
        response = self.client.patch(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        result = response.json().get("last_name")
        self.assertEqual(result, data.get("last_name"))

    def test_author_delete(self):
        """Тест удаления автора."""
        url = reverse("library:authors_delete", args=(self.author.id,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Author.objects.all().count(), 0)

    def test_author_list(self):
        """Тест вывода списка авторов."""
        url = reverse("library:authors")
        response = self.client.get(url)
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": self.author.id,
                    "last_name": self.author.last_name,
                    "first_name": self.author.first_name,
                    "patronymic": self.author.patronymic,
                    "birth_date": None,
                    "death_date": None,
                    "authors_books": [],
                }
            ],
        }

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), result)


class BookTestCase(APITestCase):
    """Тесты для модели книг."""

    def setUp(self):
        self.user = User.objects.create(email="test@test.com", is_staff=True)
        self.author = Author.objects.create(
            last_name="Test", first_name="Test", patronymic="Test"
        )
        self.book = Book.objects.create(
            title="Test_Book", author=self.author, genre="Test", description="Test"
        )
        self.client.force_authenticate(user=self.user)

    def test_book_retrieve(self):
        """Тест подробного просмотра книги."""
        url = reverse("library:books_retrieve", args=(self.book.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        result = response.json().get("title")
        self.assertEqual(result, self.book.title)

    def test_book_create(self):
        """Тест создания книги."""
        data = {
            "title": "Test_new",
            "genre": "Test_new",
            "description": "Test_new",
            "author": self.author.id,
        }
        url = reverse("library:books_create")
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.all().count(), 2)

    def test_book_update(self):
        """Тест изменения книги."""
        data = {"title": "Test_new", "genre": "Test_new", "description": "Test_new"}
        url = reverse("library:books_update", args=(self.book.id,))
        response = self.client.patch(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        result = response.json().get("title")
        self.assertEqual(result, data.get("title"))

    def test_book_delete(self):
        """Тест удаления книги."""
        url = reverse("library:books_delete", args=(self.book.id,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.all().count(), 0)

    def test_book_list(self):
        """Тест вывода списка книг."""
        url = reverse("library:books")
        response = self.client.get(url)
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": self.book.id,
                    "title": self.book.title,
                    "description": self.book.description,
                    "image": None,
                    "genre": self.book.genre,
                    "publication_year": None,
                    "publishing": None,
                    "book_year": None,
                    "isbn": None,
                    "issue": False,
                    "issue_date": None,
                    "return_date": None,
                    "author": self.author.id,
                    "reader": None,
                }
            ],
        }

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), result)


class BookIssuesTestCase(APITestCase):
    """Тесты выдачи и приёма книги."""

    def setUp(self):
        self.user = User.objects.create(email="test@test.com", is_staff=True)
        self.author = Author.objects.create(
            last_name="Test", first_name="Test", patronymic="Test"
        )
        self.book = Book.objects.create(
            title="Test_Book", author=self.author, genre="Test", description="Test"
        )
        self.book_issued = Book.objects.create(
            title="Test_Book",
            author=self.author,
            genre="Test",
            description="Test",
            issue=True,
            reader=self.user,
        )
        self.client.force_authenticate(user=self.user)

    def test_book_issue(self):
        """Тест выдачи книги."""
        url = reverse("library:book_issue")
        data = {"user": self.user.id, "book": self.book.id}
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get("message"), "Книга выдана")

    def test_book_unissue(self):
        """Тест приёма книги."""
        url = reverse("library:book_issue")
        data = {"user": self.user.id, "book": self.book_issued.id}
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get("message"), "Книга возвращена")
