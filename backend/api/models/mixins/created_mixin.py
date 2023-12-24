from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


class CreatedMixin(models.Model):
    """
    情報作成ミックスイン抽象モデル
    """

    class Meta:
        abstract = True

    # 作成者
    created_user: models.ForeignKey = models.ForeignKey(
        User,
        blank=True,
        null=True,
        on_delete=models.PROTECT,
        related_name="created_%(class)s_set",
        verbose_name=_("Created User"),
        db_comment=str(_("Created User")),
    )
    # 作成日時
    created_at: models.DateTimeField = models.DateTimeField(
        auto_now_add=True,
        db_comment=str(_("Created At")),
    )
