from django.db import models
from django.utils.translation import gettext_lazy as _


class SEOMixin(models.Model):
    """SEO ミックスイン抽象モデル．"""

    class Meta:
        abstract = True

    # メタタイトル
    meta_title: models.CharField = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name=_("Meta Title"),
    )
    # メタディスクリプション
    meta_description: models.TextField = models.TextField(
        blank=True,
        null=True,
        verbose_name=_("Meta Description"),
    )
    # メタキーワード
    meta_keywords: models.TextField = models.TextField(
        blank=True,
        null=True,
        verbose_name=_("Meta Keywords"),
    )
