from django.apps import apps
from django.db import models
from django.utils.translation import gettext_lazy as _

from api.models.languages import Languages
from api.models.mixins import (
    CreatedMixin,
    LinkMixin,
    SEOMixin,
    StatusMixin,
    UpdatedMixin,
)
from one.commons import constants


class Media(LinkMixin, SEOMixin, StatusMixin, CreatedMixin, UpdatedMixin):
    """メディアモデル．"""

    class Meta:
        db_table = constants.CODE_SEP_UNDERSCORE.join(
            [apps.get_app_config("api").name, "media"]
        )
        verbose_name = verbose_name_plural = _("Media")
        ordering = ["-sort_order", "-date_created"]

    # メディア名
    name: models.CharField = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        verbose_name=_("File Name"),
    )
    # ファイル名
    file_name: models.CharField = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        verbose_name=_("Media File Name"),
    )
    # ファイルパス
    file: models.FileField = models.FileField(
        upload_to=constants.DIR_UPLOAD,
        blank=False,
        null=False,
        verbose_name=_("Media File Path"),
    )
    # 縮小画像のパス
    thumb: models.FilePathField = models.FilePathField(verbose_name=_("Thumbnail Path"))
    # 概要
    overview: models.TextField = models.TextField(
        blank=True,
        null=True,
        verbose_name=_("Media Overview"),
    )
    # 言語
    language: models.ForeignKey = models.ForeignKey(
        Languages,
        blank=False,
        null=False,
        on_delete=models.PROTECT,
        related_name="language_%(class)s_set",
        verbose_name=_("Language"),
    )

    def __str__(self) -> str:
        return str(self.name)
