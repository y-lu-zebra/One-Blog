"""
URL 設定
"""
from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

from backend import settings

urlpatterns = [
    # API アプリ
    path("", include("api.urls")),
    # 管理サイトのドキュメント
    path(f"{settings.APP_URL_ADMIN}/doc/", include("django.contrib.admindocs.urls")),
    # 管理サイト
    path(f"{settings.APP_URL_ADMIN}/", admin.site.urls),
    # 認証
    path("api-auth/", include("rest_framework.urls")),
    # バックエンドの favicon
    path("favicon.ico", RedirectView.as_view(url="static/favicon.ico")),
]
