from api.models import Categories
from api.serializers import CategorySerializer
from api.views.ob_view_set import OBViewSet


class CategoryViewSet(OBViewSet):
    """
    カテゴリービューセット
    """

    queryset = Categories.objects.order_by("-sort_order")
    serializer_class = CategorySerializer
