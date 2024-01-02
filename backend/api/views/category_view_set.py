from api.filters import CategoryFilter
from api.models import Categories
from api.serializers import CategorySerializer
from api.views.ob_view_set import OBViewSet


class CategoryViewSet(OBViewSet):
    """
    カテゴリービューセット
    """

    queryset = Categories.objects.filter(is_published=True).all()
    serializer_class = CategorySerializer
    filterset_class = CategoryFilter
