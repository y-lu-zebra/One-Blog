from django.urls import include, path
from rest_framework import routers

from .views import CategoryViewSet, SeriesViewSet

router = routers.DefaultRouter()
router.register("categories", CategoryViewSet)
router.register("series", SeriesViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
