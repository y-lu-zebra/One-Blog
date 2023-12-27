from django.contrib import admin
from django.utils.translation import gettext as _

from api.models import Categories


@admin.register(Categories)
class CategoryAdmin(admin.ModelAdmin):
    """
    カテゴリー ADMIN
    """

    # 一覧画面に表示するフィールド
    list_display = [
        # カテゴリー名
        "name",
        # タイプ
        "type",
        # カテゴリー別名
        "alias",
        # 最終更新日時
        "date_updated",
    ]
    # 一覧画面にリンクで表示するフィールド
    list_display_links = [
        # カテゴリー名
        "name",
    ]
    # 新規作成画面に表示するフィールド構成
    fieldsets = [
        (
            None,
            {
                "fields": [
                    # カテゴリー名
                    "name",
                    # タイプ
                    "type",
                    # 親カテゴリー
                    "parent",
                    # 並び順
                    "sort_order",
                    # 作成者
                    "user_created",
                    # 最終更新者
                    "user_updated",
                ],
            },
        ),
        # オプション
        (
            _("Advanced options"),
            {
                "classes": ["collapse"],
                "fields": [
                    "alias",
                    "url",
                ],
            },
        ),
        # SEO
        (
            _("SEO Information"),
            {
                "classes": ["collapse"],
                "fields": [
                    "meta_title",
                    "meta_description",
                    "meta_keywords",
                ],
            },
        ),
    ]
