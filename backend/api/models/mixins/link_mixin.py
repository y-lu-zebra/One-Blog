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
        blank=False,
        null=False,
        verbose_name=_("Alias"),
        db_comment=str(_("Alias")),
    )
    # URL
    url: models.CharField = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name=_("URL"),
        db_comment=str(_("URL")),
    )
    # 並び順
    sort_order: models.PositiveIntegerField = models.PositiveIntegerField(
        blank=True,
        null=True,
        verbose_name=_("Sort Order"),
        db_comment=str(_("Sort Order")),
    )
