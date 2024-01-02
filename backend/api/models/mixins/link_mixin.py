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
        help_text=_(
            "When you click on a post with a URL set, "
            "you will be redirected to this URL."
        ),
    )
    # 並び順
    sort_order: models.PositiveIntegerField = models.PositiveIntegerField(
        blank=False,
        null=False,
        default=0,
        verbose_name=_("Sort Order"),
        help_text=_("Posts with a larger value will be displayed at the top."),
    )
    # ヒット数
    hits_count: models.PositiveIntegerField = models.PositiveIntegerField(
        blank=False,
        null=False,
        default=0,
        verbose_name=_("Hits Count"),
    )
