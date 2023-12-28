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

    def save_model(self, request, instance, form, change):
        """
        作成者と最終更新者の自動追加

        Parameters
        ----------
        request     リクエスト
        instance    インスタンス
        form        フォーム
        change      変更

        Returns
        -------
            加工済みのインスタンス
        """

        if not change or not instance.user_created:
            instance.user_created = request.user
        instance.user_updated = request.user
        instance.save()
        form.save_m2m()

        return instance
