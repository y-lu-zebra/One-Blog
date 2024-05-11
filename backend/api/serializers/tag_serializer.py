from api.models import Tags
from api.serializers.ob_serializer import OBSerializer
from api.serializers.user_serializer import UserSerializer


class TagSerializer(OBSerializer):
    """タグシリアライザー．"""

    # 作成者
    user_created = UserSerializer(many=False, read_only=True)
    # 最終更新者
    user_updated = UserSerializer(many=False, read_only=True)

    class Meta:
        model = Tags
        depth = 1
        # 表示フィールド
        fields = [
            # シリーズ名
            "name",
        ] + OBSerializer.MIXIN_FIELDS
        # 読み取り専用フィールド
        read_only_fields = OBSerializer.READ_ONLY_FIELDS
