from django.db import models
from django.utils.translation import gettext_lazy as _


class StatusMixin(models.Model):
    """ステータスミックスイン抽象モデル．"""

    class Meta:
        abstract = True

    # 公開フラグ
    is_published: models.BooleanField = models.BooleanField(
        blank=False,
        null=False,
        default=False,
        verbose_name=_("Is Published"),
    )
