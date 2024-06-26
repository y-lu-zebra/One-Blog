"""URL 設定."""

from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path
from django.utils.translation import gettext as _

from one import settings

# 管理サイト名変更
admin.site.site_title = settings.APP_NAME + " " + _("Admin Site")
# 管理サイトヘッダー変更
admin.site.site_header = admin.site.site_title
# インデックスページタイトル変更
admin.site.index_title = _("Dashboard")

urlpatterns = [
    # API アプリ
    path(
        f"{settings.URL_PREFIX}",
        include("api.urls"),
    ),
    # 管理サイトのドキュメント
    path(
        f"{settings.URL_PREFIX}{settings.APP_URL_ADMIN}/doc/",
        include("django.contrib.admindocs.urls"),
    ),
    # 管理サイト
    path(
        f"{settings.URL_PREFIX}{settings.APP_URL_ADMIN}/",
        admin.site.urls,
    ),
    # 認証
    path(
        "{settings.URL_PREFIX}api-auth/",
        include("rest_framework.urls"),
    ),
] + staticfiles_urlpatterns()
