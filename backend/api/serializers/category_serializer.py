from api.models import Categories
from api.serializers.ob_serializer import OBSerializer


class CategorySerializer(OBSerializer):
    """
    カテゴリーシリアライザー
    """

    class Meta:
        model = Categories
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
