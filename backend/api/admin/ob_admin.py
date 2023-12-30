from django.contrib import admin
from django.utils.translation import gettext as _


class OBAdmin(admin.ModelAdmin):
    """
    基底 ADMIN
    """

    # 一覧画面用の共通表示フィールド
    COMMON_LIST_DISPLAY_FIELDS = [
        # ヒット数
        "hits_count",
        # 並び順
        "sort_order",
        # 公開フラグ
        "is_published",
        # 作成者
        "user_created",
        # 作成日時
        "date_created",
        # 最終更新者
        "user_updated",
        # 最終更新日時
        "date_updated",
    ]
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

        return instance
