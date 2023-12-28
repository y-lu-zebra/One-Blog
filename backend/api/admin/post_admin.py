from django.contrib import admin

from api.admin.ob_admin import OBAdmin
from api.admin.post_tag_rel_inline import PostTagRelInline
from api.models import Posts


@admin.register(Posts)
class PostAdmin(OBAdmin):
    """
    投稿 ADMIN
    """

    # 一覧画面に表示するフィールド
    list_display = [
        # タイトル
        "title",
    ] + OBAdmin.COMMON_LIST_DISPLAY_FIELDS
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
                    # 内容
                    "content",
                    # タグ
                    # "tags",
                    # カテゴリー, シリーズ
                    ("category", "series"),
                    # 並び順
                    "sort_order",
                ],
            },
        ),
    ] + OBAdmin.COMMON_FIELDSETS
    # 中間モデルを利用
    inlines = [PostTagRelInline]
