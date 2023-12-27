from django_filters import rest_framework as filters  # type: ignore

from api.models import Categories


class CategoryFilter(filters.FilterSet):
    """
    カテゴリーフィルター
    """

    # カテゴリー名
    name = filters.CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = Categories
        fields = [
            # カテゴリー名
            "name",
            # タイプ
            "type",
        ]
