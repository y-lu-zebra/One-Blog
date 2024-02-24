from api.models import Series
from api.serializers.ob_serializer import OBSerializer
from api.serializers.user_serializer import UserSerializer


class SeriesSerializer(OBSerializer):
    """
    シリーズシリアライザー
    """

    # 作成者
    user_created = UserSerializer(many=False, read_only=True)
    # 最終更新者
    user_updated = UserSerializer(many=False, read_only=True)

    class Meta:
        model = Series
        depth = 1
        # 表示フィールド
        fields = [
            # シリーズ名
            "name",
            # 親シリーズ
            "parent",
        ] + OBSerializer.MIXIN_FIELDS
        # 読み取り専用フィールド
        read_only_fields = OBSerializer.READ_ONLY_FIELDS
