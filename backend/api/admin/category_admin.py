from django.contrib import admin

from api.models import Categories


class CategoryAdmin(admin.ModelAdmin):
    """
    カテゴリー ADMIN
    """

    list_display = [
        # カテゴリー名
        "name",
        # タイプ
        "type",
        # カテゴリー別名
        "alias",
        # 最終更新日時
        "updated_at",
    ]
    list_display_links = [
        # カテゴリー名
        "name",
    ]


admin.site.register(Categories, CategoryAdmin)
