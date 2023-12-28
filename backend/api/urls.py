from django.urls import include, path
from rest_framework import routers

from .views import CategoryViewSet, SeriesViewSet, TagViewSet

router = routers.DefaultRouter()
router.register("categories", CategoryViewSet)
router.register("series", SeriesViewSet)
router.register("tags", TagViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
