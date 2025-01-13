# Advanced API Project

## Views Configuration

## Filtering, Searching, and Ordering

### Filtering

You can filter the list of books by title, author, and publication year.

Example:Objective: Enhance the usability and functionality of your API by implementing filtering, searching, and ordering capabilities. This task focuses on providing users with the tools to easily access and manipulate the data presented through your API. Task Description: For this task within your advanced_api_project, you will add advanced query capabilities to your existing views that manage the Book model. This will allow API consumers to filter, search, and order the books based on different criteria. Step 1: Set Up Filtering Action Items: Integrate Django REST Framework’s filtering capabilities to allow users to filter the book list by various attributes like title, author, and publication_year. Use DRF’s DjangoFilterBackend or similar tools to set up comprehensive filtering options in your ListView. Step 2: Implement Search Functionality Search Setup: Enable search functionality on one or more fields of the Book model, such as title and author. Configure the SearchFilter in your API to allow users to perform text searches on these fields. Step 3: Configure Ordering Ordering Configuration: Allow users to order the results by any field of the Book model, particularly title and publication_year. Set up the OrderingFilter to provide front-end flexibility in sorting query results. Step 4: Update API Views View Modifications: Adjust your BookListView to incorporate filtering, searching, and ordering functionalities. Ensure that these capabilities are clearly defined and integrated into the view logic. Step 5: Test API Functionality Testing Guidelines: Test the filtering, searching, and ordering features to ensure they work correctly. Use API testing tools like Postman or curl to make requests with various query parameters to evaluate how the API handles them. Step 6: Document the Implementation Documentation Requirements: Detail how filtering, searching, and ordering were implemented in your views. Include examples of how to use these features in API requests in the project documentation or code comments.
Let's enhance the usability and functionality of your API by adding filtering, searching, and ordering capabilities to the Book model views in your advanced_api_project.

Step 1: Set Up Filtering
Action Items: Integrate Django REST Framework’s filtering capabilities to allow users to filter the book list by various attributes like title, author, and publication_year.

Code Implementation:

Install django-filter:

bash
pip install django-filter
Update settings.py to include django_filters:

python
INSTALLED_APPS = [
    ...
    'django_filters',
]
Create a filter class in api/filters.py:

python
from django_filters import rest_framework as filters
from .models import Book

class BookFilter(filters.FilterSet):
    class Meta:
        model = Book
        fields = {
            'title': ['exact', 'icontains'],
            'author__name': ['exact', 'icontains'],
            'publication_year': ['exact', 'gte', 'lte'],
        }
Update BookListView to include filtering in api/views.py:

python
from django_filters.rest_framework import DjangoFilterBackend

class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = BookFilter
Step 2: Implement Search Functionality
Search Setup: Enable search functionality on one or more fields of the Book model, such as title and author.

Code Implementation:

Update BookListView to include search functionality in api/views.py:

python
from rest_framework.filters import SearchFilter

class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = BookFilter
    search_fields = ['title', 'author__name']
Step 3: Configure Ordering
Ordering Configuration: Allow users to order the results by any field of the Book model, particularly title and publication_year.

Code Implementation:

Update BookListView to include ordering functionality in api/views.py:

python
from rest_framework.filters import OrderingFilter

class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = BookFilter
    search_fields = ['title', 'author__name']
    ordering_fields = ['title', 'publication_year']
Step 4: Update API Views
View Modifications: Adjust your BookListView to incorporate filtering, searching, and ordering functionalities. This has been demonstrated in the previous steps.

Step 5: Test API Functionality
Testing Guidelines: Use API testing tools like Postman or curl to make requests with various query parameters to evaluate how the API handles them.

Examples of API Requests:

Filter by title:

GET /api/books/?title=Harry
Search by author name:

GET /api/books/?search=Rowling
Order by publication year:

GET /api/books/?ordering=publication_year
Combine filtering and ordering:

GET /api/books/?title=Harry&ordering=publication_year
Step 6: Document the Implementation
Documentation Requirements: Detail how filtering, searching, and ordering were implemented in your views. Include examples of how to use these features in API requests in the project documentation or code comments.

Add Comments to api/views.py:

python

# ListView for retrieving all books with filtering, searching, and ordering capabilities

class BookListView(generics.ListCreateAPIView):
    """
    get:
    Return a list of all existing books with filtering, searching, and ordering options.

    post:
    Create a new book instance.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = BookFilter
    search_fields = ['title', 'author__name']
    ordering_fields = ['title', 'publication_year']
Update your README.md:

markdown

# Advanced API Project

## Filtering, Searching, and Ordering

### Filtering

You can filter the list of books by title, author, and publication year.

Example:
GET /api/books/?title=Harry&author__name=Rowling&publication_year__gte=1990

### BookListView

- **URL:** `/books/`
- **Methods:** `GET`, `POST`
- **Description:** Retrieve all books or create a new book.

### BookDetailView

- **URL:** `/books/<int:pk>/`
- **Methods:** `GET`, `PUT`, `DELETE`
- **Description:** Retrieve, update, or delete a book by ID.

### BookCreateView

- **URL:** `/books/create/`
- **Methods:** `POST`
- **Description:** Create a new book instance.

### BookUpdateView

- **URL:** `/books/<int:pk>/update/`
- **Methods:** `PUT`
- **Description:** Update an existing book instance.

### BookDeleteView

- **URL:** `/books/<int:pk>/delete/`
- **Methods:** `DELETE`
- **Description:** Delete a book instance.

## Permissions

- **BookCreateView, BookUpdateView, BookDeleteView:** Restricted to authenticated users only.
- **BookListView, BookDetailView:** Read-only access allowed for unauthenticated users.

## Testing

Manually test each view using tools like Postman or `curl` to ensure they function as expected and permissions are enforced correctly.
