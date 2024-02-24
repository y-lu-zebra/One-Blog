from django.urls import include, path
from rest_framework import routers

from .views import CategoryViewSet, PostViewSet, SeriesViewSet, TagViewSet

router = routers.DefaultRouter()
router.register("categories", CategoryViewSet)
router.register("posts", PostViewSet)
router.register("series", SeriesViewSet)
router.register("tags", TagViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
