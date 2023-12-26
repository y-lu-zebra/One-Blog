"""
URL 設定
"""
from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

from backend import settings
from backend.commons import constants

urlpatterns = [
    path("", include("api.urls")),
    path(f"{settings.APP_URL_ADMIN}{constants.CODE_SEP_URL}", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("favicon.ico", RedirectView.as_view(url="static/favicon.ico")),
]
