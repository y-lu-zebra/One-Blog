from django.contrib import admin

from api.admin.ob_admin import OBAdmin
from api.models import Categories


@admin.register(Categories)
class CategoryAdmin(OBAdmin):
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
        # 作成者
        "user_created",
        # 作成日時
        "date_created",
        # 最終更新者
        "user_updated",
        # 最終更新日時
        "date_updated",
    ]
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
                ],
            },
        ),
    ] + OBAdmin.COMMON_FIELDSETS
