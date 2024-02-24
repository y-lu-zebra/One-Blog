from django.apps import AppConfig


class ApiConfig(AppConfig):
    """
    API アプリ設定クラス
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "api"
