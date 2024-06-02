from django_filters import rest_framework as filters  # type: ignore

from api.models import Series


class SeriesFilter(filters.FilterSet):
    """シリーズフィルター．"""

    # シリーズ名（あいまい検索）
    name = filters.CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = Series
        fields = [
            # シリーズ名
            "name",
            # 親カテゴリー
            "parent",
            # 言語
            "language",
        ]
