from typing import Any

from rest_framework import serializers

from api.models import Media
from api.serializers.ob_serializer import OBSerializer
from api.serializers.user_serializer import UserSerializer


class MediaSerializer(OBSerializer):
    """メディアシリアライザー．"""

    # 作成者
    user_created = UserSerializer(many=False, read_only=True)
    # 最終更新者
    user_updated = UserSerializer(many=False, read_only=True)
    # 言語
    language: Any = serializers.StringRelatedField()

    class Meta:
        model = Media
        depth = 1
        fields = [
            # メディア名
            "name",
            # ファイルパス
            "file",
        ] + OBSerializer.MIXIN_FIELDS
        # 読み取り専用フィールド
        read_only_fields = OBSerializer.READ_ONLY_FIELDS
