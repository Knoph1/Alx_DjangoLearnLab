# blog/urls.py

from django.urls import path
from django.contrib.auth import views as auth_views
from . import views 
from .views import (
  PostListView,
  PostDetailView,
  PostCreateView,
  PostUpdateView,
  PostDeleteView,
  CommentCreateView, 
  CommentUpdateView, 
  CommentDeleteView,
  search,
)

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'), 
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='add-comment'), 
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='edit-comment'), 
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='delete-comment'), 
    path('tags/<slug:tag_slug>/', PostByTagListView.as_view(), name='posts-by-tag'),
    path('search/', search, name='search'),
]


