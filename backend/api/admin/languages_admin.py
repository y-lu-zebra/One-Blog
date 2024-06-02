from typing import Any

from django.contrib import admin

from api.admin.ob_admin import OBAdmin
from api.models import Languages


@admin.register(Languages)
class LanguageAdmin(OBAdmin):
    """言語 ADMIN．"""

    # 一覧画面に表示するフィールド
    list_display: list[Any] = [
        # 言語名
        "name",
        # 言語コード
        "code",
    ] + OBAdmin.HISTORY_LIST_DISPLAY_FIELDS
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
                    # 言語名
                    "name",
                    # 言語コード
                    "code",
                ],
            },
        ),
    ]
