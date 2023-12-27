from django.contrib import admin
from django.utils.translation import gettext as _


class OBAdmin(admin.ModelAdmin):
    # 共通フィールドセット
    COMMON_FIELDSETS = [
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
