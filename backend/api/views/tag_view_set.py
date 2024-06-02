from django_filters.rest_framework import DjangoFilterBackend  # type: ignore

from api.filters import TagFilter
from api.models import Tags
from api.paginators import OnePaginator
from api.serializers import TagSerializer
from api.views.ob_view_set import OBViewSet


class TagViewSet(OBViewSet):
    """タグビューセット．"""

    queryset = Tags.objects.filter(is_published=True).all()
    serializer_class = TagSerializer
    pagination_class = OnePaginator
    filter_backends = [DjangoFilterBackend]
    filterset_class = TagFilter
