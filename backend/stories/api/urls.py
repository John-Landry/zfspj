from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import StoryViewSet

story_router = DefaultRouter()
story_router.register(r'stories', StoryViewSet)