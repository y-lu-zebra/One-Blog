from api.models import Tags
from api.serializers import TagSerializer
from api.views.ob_view_set import OBViewSet


class TagViewSet(OBViewSet):
    """
    タグビューセット
    """

    queryset = Tags.objects.order_by("-sort_order")
    serializer_class = TagSerializer
