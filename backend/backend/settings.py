"""
One Blog バックエンドの設定
"""

import os
import re
import sys

import environ  # type: ignore

from .commons import constants
from .utils import files

env = environ.Env(DEBUG=(bool, False))

# 環境設定ファイルから設定項目を読み込み
if sys.argv[1:2] == [constants.CODE_MODE_TEST]:
    """テストモードの場合"""
    environ.Env.read_env(constants.PATH_ENV_TEST)
else:
    """本番モードの場合"""
    environ.Env.read_env(constants.PATH_ENV)

# ========== Django 設定 ================================================================

# 秘密鍵
SECRET_KEY: str = env("API_SECRET_KEY")

# デバッグモード
DEBUG: bool = env.bool("API_DEBUG")

# 配信可能なホスト・ドメイン
ALLOWED_HOSTS: list[str] = env.list("API_ALLOWED_HOSTS")

# インストール済みのアプリケーション
INSTALLED_APPS: list[str] = [
    "django.contrib.admindocs",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "corsheaders",
    "rest_framework",
    "django_filters",
    "api.apps.ApiConfig",
    "admin_theme",
]

# ミドルウェア
MIDDLEWARE: list[str] = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "djangorestframework_camel_case.middleware.CamelCaseMiddleWare",
]

# ルート URLconf
ROOT_URLCONF: str = "backend.urls"

# テンプレート
TEMPLATES: list[dict] = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": constants.PATH_TEMPLATE_LIST,
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# WSGI アプリケーション
WSGI_APPLICATION = "backend.wsgi.application"

# データベース
DATABASES: dict = {
    "default": {
        "ENGINE": f"django.db.backends.{env('DB_ENGINE')}",
        "NAME": env("DB_NAME"),
        "USER": env("DB_USER"),
        "PASSWORD": env("DB_PASS"),
        "HOST": env("DB_HOST"),
        "PORT": env("DB_PORT"),
    }
}

# ユーザーパスワード妥当性検証用のバリデーター
AUTH_PASSWORD_VALIDATORS: list[dict] = [
    {
        "NAME": "django.contrib.auth.password_validation"
        ".UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# 言語コード
LANGUAGE_CODE: str = env("APP_LANGUAGE").lower()

# タイムゾーン
TIME_ZONE: str = env("APP_TIME_ZONE")

# 翻訳機能
USE_I18N: bool = True

# 時刻自動変換（タイムゾーンに合わせ）
USE_TZ: bool = True

# 翻訳ファイルの絶対パス
LOCALE_PATHS = [constants.PATH_LOCALE]

# 静的ファイルの場所（CSS, JavaScript, Images）
STATICFILES_DIRS: list[str] = constants.PATH_STATIC_LIST

# デプロイ用の静的ファイルの場所
STATIC_ROOT: str = constants.PATH_STATIC

# 静的ファイルの URL
STATIC_URL: str = f"{env('API_STATIC_URL')}{constants.CODE_SEP_URL}"

# 主キーフィールドのデフォルトタイプ
DEFAULT_AUTO_FIELD: str = "django.db.models.BigAutoField"

# ログ出力ディレクトリ作成
files.make_dir(env("LOG_DIR"))

# ロギング
LOGGING: dict = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {"format": env("LOG_FORMAT")},
    },
    "handlers": {
        "console": {
            "level": env("LOG_LEVEL"),
            "class": "logging.StreamHandler",
            "formatter": "default",
        },
        "file": {
            "level": env("LOG_LEVEL"),
            "class": "logging.handlers.RotatingFileHandler",
            "filename": os.path.join(
                env("LOG_DIR"), f"{env('LOG_NAME')}{constants.CODE_EXT_LOG}"
            ),
            "maxBytes": env.int("LOG_MAX_SIZE") * constants.HEX_BYTE,
            "backupCount": env.int("LOG_BACKUP_COUNT"),
            "formatter": "default",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["console", "file"],
            "propagate": True,
            "level": env("LOG_LEVEL"),
        },
    },
}

# ========== Django REST framework 設定 =================================================

REST_FRAMEWORK: dict = {
    # ページングクラス
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    # 一覧 API の表示件数
    "PAGE_SIZE": env.int("API_PAGE_SIZE"),
    # デフォルト・パーミッション・チェック・クラス
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly",
    ],
    # フィルター設定
    "DEFAULT_FILTER_BACKENDS": [
        "django_filters.rest_framework.DjangoFilterBackend",
    ],
    # IF キャメルケースとスネークケースの相互変換
    "DEFAULT_RENDERER_CLASSES": (
        "djangorestframework_camel_case.render.CamelCaseJSONRenderer",
        "djangorestframework_camel_case.render.CamelCaseBrowsableAPIRenderer",
    ),
    # IF キャメルケースとスネークケースの相互変換
    "DEFAULT_PARSER_CLASSES": (
        "djangorestframework_camel_case.parser.CamelCaseFormParser",
        "djangorestframework_camel_case.parser.CamelCaseMultiPartParser",
        "djangorestframework_camel_case.parser.CamelCaseJSONParser",
    ),
    # テストリクエストフォーマット
    "TEST_REQUEST_DEFAULT_FORMAT": "json",
}

# ========== CORS 設定 ==================================================================

# CORS 許可ホスト
CORS_ALLOWED_ORIGINS: list[str] = [env("APP_URL")]

# ========== One Blog 設定 ==============================================================

# アプリ名称
APP_NAME = env("APP_NAME")

# API の管理画面の URL
APP_URL_ADMIN = env("APP_URL_ADMIN")

# URL プレフィックス
m = re.findall(r"^http://.+?/(.*)$", env("API_URL"))
URL_PREFIX = m[0] + constants.CODE_SEP_URL if len(m) > 0 else ""
