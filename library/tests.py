from rest_framework.test import APITestCase
from library.models import Author, Book
from django.urls import reverse
from rest_framework import status
from users.models import User


class AuthorTestCase(APITestCase):
    """Тесты для модели авторов."""

    def setUp(self):
        self.user = User.objects.create(email="test@test.com")
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
        data = {"last_name": "Test", "first_name": "Test", "patronymic": "Test"}
        url = reverse("library:authors_create")
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Author.objects.all().count(), 2)

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


class BookTestCase(APITestCase):
    """Тесты для модели книг."""

    def setUp(self):
        self.user = User.objects.create(email="test@test.com")
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
