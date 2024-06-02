from django.apps import apps
from django.db import models
from django.utils.translation import gettext_lazy as _

from api.models.mixins import CreatedMixin, UpdatedMixin
from one.commons import constants


class Languages(CreatedMixin, UpdatedMixin):
    """言語モデル．"""

    class Meta:
        db_table = constants.CODE_SEP_UNDERSCORE.join(
            [apps.get_app_config("api").name, "languages"]
        )
        verbose_name = verbose_name_plural = _("Languages")
        ordering = ["-date_updated"]

    # 言語名
    name: models.CharField = models.CharField(
        max_length=55,
        blank=False,
        null=False,
        verbose_name=_("Language Name"),
    )
    # 言語コード
    code: models.CharField = models.CharField(
        max_length=10,
        blank=False,
        null=False,
        verbose_name=_("Language Code"),
    )

    def __str__(self) -> str:
        return str(self.name)
