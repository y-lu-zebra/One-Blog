from django.contrib import admin

from api.admin.ob_admin import OBAdmin
from api.models import Series


@admin.register(Series)
class SeriesAdmin(OBAdmin):
    """
    シリーズ ADMIN
    """

    # 一覧画面に表示するフィールド
    list_display = [
        # カテゴリー名
        "name",
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
    fieldsets: list[tuple] = [
        (
            None,
            {
                "fields": [
                    # カテゴリー名
                    "name",
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
    ] + OBAdmin.COMMON_FIELDSETS
