from django.test import TestCase

# Create your tests here.
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Book, Author
class BookAPITests(APITestCase):
    def setUp(self):
        # Create test data
        self.author = Author.objects.create(name="Test Author")
        self.book = Book.objects.create(
            title="Test Book",
            publication_year=2023,
            author=self.author
        )
        self.list_url = reverse('book-list')
        self.detail_url = reverse('book-detail', kwargs={'pk': self.book.pk})

    def test_list_books(self):
        # Test GET /books/
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('Test Book', str(response.data))

    def test_create_book(self):
        # Test POST /books/
        data = {
            "title": "New Book",
            "publication_year": 2024,
            "author": self.author.id
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_update_book(self):
        # Test PUT /books/<id>/
        data = {
            "title": "Updated Book",
            "publication_year": 2023,
            "author": self.author.id
        }
        response = self.client.put(self.detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Updated Book")

    def test_delete_book(self):
        # Test DELETE /books/<id>/
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_filter_books_by_author(self):
        # Test GET /books/?author=<author_id>
        response = self.client.get(self.list_url, {'author': self.author.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('Test Book', str(response.data))

    def test_search_books(self):
        # Test GET /books/?search=Test
        response = self.client.get(self.list_url, {'search': 'Test'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('Test Book', str(response.data))

    def test_order_books_by_title(self):
        # Test GET /books/?ordering=title
        response = self.client.get(self.list_url, {'ordering': 'title'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('Test Book', str(response.data))
