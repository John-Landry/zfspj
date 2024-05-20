from rest_framework.routers import DefaultRouter
from stories.api.urls import story_router
from django.urls import path, include

router = DefaultRouter()
#for stories app
router.registry.extend(story_router.registry)

urlpatterns = [
     path("", include(router.urls))
]
