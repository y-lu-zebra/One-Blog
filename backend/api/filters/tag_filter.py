from django_filters import rest_framework as filters  # type: ignore

from api.models import Tags


class TagFilter(filters.FilterSet):
    """タグフィルター．"""

    # タグ名（あいまい検索）
    name = filters.CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = Tags
        fields = [
            # タグ名
            "name",
            # 言語
            "language",
        ]
