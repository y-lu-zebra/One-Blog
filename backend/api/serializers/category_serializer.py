from api.models import Categories
from api.serializers.ob_serializer import OBSerializer
from api.serializers.user_serializer import UserSerializer


class CategorySerializer(OBSerializer):
    """カテゴリーシリアライザー．"""

    # 作成者
    user_created = UserSerializer(many=False, read_only=True)
    # 最終更新者
    user_updated = UserSerializer(many=False, read_only=True)

    class Meta:
        model = Categories
        depth = 1
        fields = [
            # カテゴリー名
            "name",
            # タイプ
            "type",
            # 親カテゴリー
            "parent",
        ] + OBSerializer.MIXIN_FIELDS
        # 読み取り専用フィールド
        read_only_fields = OBSerializer.READ_ONLY_FIELDS
