from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


class UpdatedMixin(models.Model):
    """
    情報更新ミックスイン抽象モデル
    """

    class Meta:
        abstract = True

    # 最終更新者
    updated_user: models.ForeignKey = models.ForeignKey(
        User,
        blank=True,
        null=True,
        on_delete=models.PROTECT,
        related_name="updated_%(class)s_set",
        verbose_name=_("Updated User"),
    )
    # 最終更新日時
    updated_at: models.DateTimeField = models.DateTimeField(
        auto_now=True,
    )
