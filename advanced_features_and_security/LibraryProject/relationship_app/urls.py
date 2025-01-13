# relationship_app/urls.py

from django.urls import path
from .import views 
from .views import list_books, LibraryDetailView
from django.contrib.auth import views as auth_views      
from .views import SignUpView
from .views import register
from .views import login_view
from .views import login
from .views import logout_view
from .views import admin_view, librarian_view, member_view


urlpatterns = [
    path('register/', auth_views.LoginView.as_view(template_name='relationship_app/register.html') , name='register'),
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'), 
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('admin/', admin_view, name='admin_view'),
    path('librarian/', librarian_view, name='librarian_view'),
    path('member/', member_view, name='member-view'),
    path('add_book/', views.add_book, name='add_book'),
    path('edit_book/<int:book_id>/', views.edit_book, name='edit_book'),
    path('delete_book/<int:book_id>/', views.delete_book, name='delete_book'),
]
