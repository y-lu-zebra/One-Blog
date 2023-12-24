"""
One Blog バックエンドの設定
"""
import sys

import environ  # type: ignore

from .commons import constants

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
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "corsheaders",
    "rest_framework",
    "api.apps.ApiConfig",
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
]

# ルート URLconf
ROOT_URLCONF: str = "backend.urls"

# テンプレート
TEMPLATES: list[dict] = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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

# 静的ファイルの場所（CSS, JavaScript, Images）
STATICFILES_DIRS: list[str] = [constants.PATH_STATIC]

# 静的ファイルの URL
STATIC_URL: str = f"{env('API_STATIC_URL')}/"

# 主キーフィールドのデフォルトタイプ
DEFAULT_AUTO_FIELD: str = "django.db.models.BigAutoField"

# ========== Django REST framework 設定 =================================================

REST_FRAMEWORK: dict = {
    # デフォルト・パーミッション・チェック・クラス
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly"
    ]
}

# ========== CORS 設定 ==================================================================

# CORS 許可ホスト
CORS_ALLOWED_ORIGINS: list[str] = [env("APP_URL")]
