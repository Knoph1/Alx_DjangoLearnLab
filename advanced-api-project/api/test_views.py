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
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from api.models import Book

class BookAPITests(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        
        # Create sample data
        self.book = Book.objects.create(title='Test Book', author='Test Author', publication_year=2023)
        
        # Define the API endpoints
        self.list_url = '/api/books/'

    def test_authenticated_access(self):
        # Log in as the test user
        self.client.login(username='testuser', password='testpassword')

        # Make a GET request to the API
        response = self.client.get(self.list_url)

        # Assert that the response is successful
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_unauthenticated_access(self):
        # Make a GET request without logging in
        response = self.client.get(self.list_url)

        # Assert that access is forbidden
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
from rest_framework.test import APIRequestFactory
from rest_framework.authtoken.models import Token
from api.views import BookListView

factory = APIRequestFactory()
user = User.objects.create_user(username='testuser', password='testpassword')
token = Token.objects.create(user=user)

request = factory.get('/api/books/')
force_authenticate(request, user=user)
response = BookListView.as_view()(request)
