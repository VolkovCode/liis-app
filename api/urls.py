from django.urls import path, include

from rest_framework.routers import DefaultRouter
from .views import PostViewSet, RegisterView, PostFollowViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'follow-posts', PostFollowViewSet, basename='follow-post')


urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
]


