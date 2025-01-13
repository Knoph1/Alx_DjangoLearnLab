from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Authentication URLs
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'),

    # Role-based URLs
    path('admin/', views.admin_view, name='admin_view'),
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('member/', views.member_view, name='member_view'),

    # Book and Library URLs
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),

    # CRUD operations for books
    path('add/', views.add_book, name='add_book'),
    path('edit/<int:pk>/', views.edit_book, name='edit_book'),
    path('delete/<int:pk>/', views.delete_book, name='delete_book'),

    # Include URLs for relationship app
    path('relationship_app/', include('relationship_app.urls')),
]

# Main project URL configuration
from django.contrib import admin

urlpatterns += [
    path('admin/', admin.site.urls),
]

from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.book_list, name='book_list'),  # URL for the list of books
    path('books/<int:book_id>/', views.books, name='books'),  # URL for a single book
]
