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


class Series(LinkMixin, SEOMixin, StatusMixin, CreatedMixin, UpdatedMixin):
    """シリーズモデル．"""

    class Meta:
        db_table = constants.CODE_SEP_UNDERSCORE.join(
            [apps.get_app_config("api").name, "series"]
        )
        verbose_name = verbose_name_plural = _("Series")
        ordering = ["-sort_order", "-date_updated"]

    # シリーズ名
    name: models.CharField = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        verbose_name=_("Series Name"),
    )
    # 親シリーズ
    parent: models.ForeignKey = models.ForeignKey(
        "self",
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        verbose_name=_("Parent Series"),
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
