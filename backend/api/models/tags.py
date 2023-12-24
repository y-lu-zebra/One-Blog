from django.apps import apps
from django.db import models
from django.utils.translation import gettext_lazy as _

from api.models.mixins import CreatedMixin, LinkMixin, SEOMixin, UpdatedMixin
from backend.commons import constants


class Tags(LinkMixin, SEOMixin, CreatedMixin, UpdatedMixin):
    """
    タグモデル
    """

    class Meta:
        db_table = constants.CODE_SEP_UNDERSCORE.join(
            [apps.get_app_config("api").name, "tags"]
        )
        verbose_name = verbose_name_plural = _("Tags")

    # タグ名
    name: models.CharField = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        verbose_name=_("Tag Name"),
        db_comment=str(_("Tag Name")),
    )
