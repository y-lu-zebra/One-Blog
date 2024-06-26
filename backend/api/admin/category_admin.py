from typing import Any

from django.contrib import admin

from api.admin.ob_admin import OBAdmin
from api.models import Categories


@admin.register(Categories)
class CategoryAdmin(OBAdmin):
    """カテゴリー ADMIN．"""

    # 一覧画面に表示するフィールド
    list_display: list[Any] = (
        [
            # カテゴリー名
            "name",
            # タイプ
            "type",
        ]
        + OBAdmin.COMMON_LIST_DISPLAY_FIELDS
        + OBAdmin.HISTORY_LIST_DISPLAY_FIELDS
    )
    # 一覧画面にリンクで表示するフィールド
    list_display_links = [
        # カテゴリー名
        "name",
    ]
    # 新規作成画面に表示するフィールド構成
    fieldsets: list[tuple] = [
        (
            None,
            {
                "fields": [
                    # カテゴリー名
                    "name",
                    # タイプ
                    "type",
                    # 並び順
                    "sort_order",
                    # 親カテゴリー
                    "parent",
                    # 公開フラグ
                    "is_published",
                ],
            },
        ),
    ] + OBAdmin.COMMON_FIELDSETS
