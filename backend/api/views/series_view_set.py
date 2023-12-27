from api.models import Series
from api.serializers import SeriesSerializer
from api.views.ob_view_set import OBViewSet


class SeriesViewSet(OBViewSet):
    """
    シリーズビューセット
    """

    queryset = Series.objects.order_by("-sort_order")
    serializer_class = SeriesSerializer
