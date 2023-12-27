from api.models import Categories
from api.serializers.ob_serializer import OBSerializer
from api.serializers.user_serializer import UserSerializer


class CategorySerializer(OBSerializer):
    """
    カテゴリーシリアライザー
    """

    # 作成者
    created_user = UserSerializer(many=False, read_only=True)
    # 最終更新者
    updated_user = UserSerializer(many=False, read_only=True)

    class Meta:
        model = Categories
        depth = 1
        fields = [
            # カテゴリー ID
            "id",
            # カテゴリー名
            "name",
            # タイプ
            "type",
            # 親カテゴリー
            "parent",
            # カテゴリー別名
            "alias",
            # URL
            "url",
            # 並び順
            "sort_order",
            # メタタイトル
            "meta_title",
            # メタディスクリプション
            "meta_description",
            # メタキーワード
            "meta_keywords",
            # 作成者
            "created_user",
            # 作成日時
            "created_at",
            # 最終更新者
            "updated_user",
            # 最終更新日時
            "updated_at",
        ]
        read_only_fields = [
            # 作成者
            "created_user",
            # 作成日時
            "created_at",
            # 最終更新者
            "updated_user",
            # 最終更新日時
            "updated_at",
        ]
