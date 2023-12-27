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
    user_updated: models.ForeignKey = models.ForeignKey(
        User,
        blank=False,
        null=False,
        on_delete=models.PROTECT,
        related_name="updated_%(class)s_set",
        verbose_name=_("Updated User"),
    )
    # 最終更新日時
    date_updated: models.DateTimeField = models.DateTimeField(
        auto_now=True,
    )
