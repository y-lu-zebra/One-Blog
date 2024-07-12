from typing import Any

from django.contrib import admin

from api.admin.ob_admin import OBAdmin
from api.models import Media


@admin.register(Media)
class MediaAdmin(OBAdmin):
    """メディア ADMIN．"""

    # 一覧画面に表示するフィールド
    list_display: list[Any] = (
        [
            # タイトル
            "title",
        ]
        + OBAdmin.COMMON_LIST_DISPLAY_FIELDS
        + OBAdmin.HISTORY_LIST_DISPLAY_FIELDS
    )
    # 一覧画面にリンクで表示するフィールド
    list_display_links = [
        # タイトル
        "title",
    ]
    # 新規作成画面に表示するフィールド構成
    fieldsets: list[tuple] = [
        (
            None,
            {
                "fields": [
                    # タイトル
                    "title",
                    # 概要
                    "overview",
                    # カテゴリー
                    "file",
                    # 並び順
                    "sort_order",
                    # 公開フラグ
                    "is_published",
                ],
            },
        ),
    ] + OBAdmin.COMMON_FIELDSETS
    # 中間モデルを利用
    # inlines = [PostTagRelInline, PostSeriesRelInline]
