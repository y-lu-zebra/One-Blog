from django_filters.rest_framework import DjangoFilterBackend  # type: ignore

from api.filters import SeriesFilter
from api.models import Series
from api.serializers import SeriesSerializer
from api.views.ob_view_set import OBViewSet


class SeriesViewSet(OBViewSet):
    """シリーズビューセット．"""

    queryset = Series.objects.filter(is_published=True).all()
    serializer_class = SeriesSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = SeriesFilter
