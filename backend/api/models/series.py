from django.apps import apps
from django.db import models
from django.utils.translation import gettext_lazy as _

from api.models.mixins import CreatedMixin, LinkMixin, SEOMixin, UpdatedMixin
from backend.commons import constants


class Series(LinkMixin, SEOMixin, CreatedMixin, UpdatedMixin):
    """
    シリーズモデル
    """

    class Meta:
        db_table = constants.CODE_SEP_UNDERSCORE.join(
            [apps.get_app_config("api").name, "series"]
        )
        verbose_name = verbose_name_plural = _("Series")

    # シリーズ名
    name: models.CharField = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        verbose_name=_("Series Name"),
        db_comment=str(_("Series Name")),
    )
    # 親シリーズ
    parent: models.ForeignKey = models.ForeignKey(
        "self",
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        verbose_name=_("Parent Series"),
        db_comment=str(_("Parent Series")),
    )
