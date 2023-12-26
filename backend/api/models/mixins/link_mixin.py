from django.db import models
from django.utils.translation import gettext_lazy as _


class LinkMixin(models.Model):
    """
    リンクミックスイン抽象モデル
    """

    class Meta:
        abstract = True

    # カテゴリー別名
    alias: models.CharField = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name=_("Alias"),
    )
    # URL
    url: models.CharField = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name=_("URL"),
    )
    # 並び順
    sort_order: models.PositiveIntegerField = models.PositiveIntegerField(
        blank=True,
        null=True,
        verbose_name=_("Sort Order"),
    )
