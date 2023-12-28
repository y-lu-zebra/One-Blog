from api.models import Posts
from api.serializers.ob_serializer import OBSerializer
from api.serializers.user_serializer import UserSerializer


class PostSerializer(OBSerializer):
    """
    投稿シリアライザー
    """

    # 作成者
    user_created = UserSerializer(many=False, read_only=True)
    # 最終更新者
    user_updated = UserSerializer(many=False, read_only=True)

    class Meta:
        model = Posts
        depth = 1
        fields = [
            # タイトル
            "title",
            # 概要
            "overview",
            # 内容
            "content",
            # カテゴリー
            "category",
            # シリーズ
            "series",
            # タグ
            "tags",
        ] + OBSerializer.MIXIN_FIELDS
        # 読み取り専用フィールド
        read_only_fields = OBSerializer.READ_ONLY_FIELDS
