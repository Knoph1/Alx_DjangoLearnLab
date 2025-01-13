from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = router.urls
from django.urls import path
from .views import UserFeedView

urlpatterns = [
    path('feed/', UserFeedView.as_view(), name='user-feed'),
]
from django.urls import path
from .views import LikePostView, UnlikePostView

urlpatterns = [
    path('<int:pk>/like/', LikePostView.as_view(), name='like-post'),
    path('<int:pk>/unlike/', UnlikePostView.as_view(), name='unlike-post'),
]
from django.urls import path
from .views import FeedView

urlpatterns = [
    path('feed/', FeedView.as_view(), name='user_feed'),
]
