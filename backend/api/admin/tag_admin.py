from typing import Any

from django.contrib import admin

from api.admin.ob_admin import OBAdmin
from api.admin.post_tag_rel_inline import PostTagRelInline
from api.models import Tags


@admin.register(Tags)
class TagAdmin(OBAdmin):
    """タグ ADMIN．"""

    # 一覧画面に表示するフィールド
    list_display: list[Any] = [
        # カテゴリー名
        "name",
    ] + OBAdmin.COMMON_LIST_DISPLAY_FIELDS
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
                    # 並び順
                    "sort_order",
                    # 公開フラグ
                    "is_published",
                ],
            },
        ),
    ] + OBAdmin.COMMON_FIELDSETS
    # 中間モデルを利用
    inlines = [PostTagRelInline]
