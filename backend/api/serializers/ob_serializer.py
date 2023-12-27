import logging

from rest_framework import serializers


class OBSerializer(serializers.ModelSerializer):
    """
    基底シリアライザー
    """

    # ミックスインフィールド
    MIXIN_FIELDS = [
        # ID（主キー）
        "id",
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
        "user_created",
        # 作成日時
        "date_created",
        # 最終更新者
        "user_updated",
        # 最終更新日時
        "date_updated",
    ]
    # 読み取り専用フィールド
    READ_ONLY_FIELDS = [
        # 作成者
        "user_created",
        # 作成日時
        "date_created",
        # 最終更新者
        "user_updated",
        # 最終更新日時
        "date_updated",
    ]

    # ロガー
    logger = logging.getLogger("django")
