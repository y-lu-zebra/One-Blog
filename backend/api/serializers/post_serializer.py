from typing import Any

from rest_framework import serializers

from api.models import Posts
from api.serializers.ob_serializer import OBSerializer
from api.serializers.series_serializer import SeriesSerializer
from api.serializers.tag_serializer import TagSerializer
from api.serializers.user_serializer import UserSerializer


class PostSerializer(OBSerializer):
    """
    投稿シリアライザー
    """

    # カテゴリー
    category = serializers.SerializerMethodField("get_category")
    # シリーズ
    series = serializers.SerializerMethodField("get_series")
    # タグ
    tags = serializers.SerializerMethodField("get_tags")
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

    def get_category(self, obj) -> dict:
        """
        カテゴリー取得処理
        （公開済みのカテゴリーデータのみ）

        Parameters
        ----------
        obj
            投稿オブジェクト
        Returns
        -------
            投稿と紐付きのカテゴリー
        """

        rst: dict[Any, Any] = {}
        if obj.category and obj.category.is_published:
            rst = SeriesSerializer(instance=obj.category, context=self.context).data

        return rst

    def get_series(self, obj) -> dict:
        """
        シリーズ取得処理
        （公開済みのシリーズデータのみ）

        Parameters
        ----------
        obj
            投稿オブジェクト
        Returns
        -------
            投稿と紐付きのシリーズの辞書
        """

        return SeriesSerializer(
            instance=obj.series.all().filter(is_published=True),
            many=True,
            context=self.context,
        ).data

    def get_tags(self, obj) -> dict:
        """
        タグ取得処理
        （公開済みのタグデータのみ）

        Parameters
        ----------
        obj
            投稿オブジェクト
        Returns
        -------
            投稿と紐付きのタグの辞書
        """

        return TagSerializer(
            instance=obj.tags.all().filter(is_published=True),
            many=True,
            context=self.context,
        ).data
