from django.apps import apps
from django.db import models
from django.utils.translation import gettext_lazy as _

from api.models.categories import Categories
from api.models.mixins import (
    CreatedMixin,
    LinkMixin,
    SEOMixin,
    StatusMixin,
    UpdatedMixin,
)
from api.models.series import Series
from api.models.tags import Tags
from one.commons import constants


class Posts(LinkMixin, SEOMixin, StatusMixin, CreatedMixin, UpdatedMixin):
    """投稿モデル．"""

    class Meta:
        db_table = constants.CODE_SEP_UNDERSCORE.join(
            [apps.get_app_config("api").name, "posts"]
        )
        verbose_name = verbose_name_plural = _("Posts")
        ordering = ["-sort_order", "-date_updated"]

    # タイトル
    title: models.CharField = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        verbose_name=_("Post Title"),
    )
    # 概要
    overview: models.TextField = models.TextField(
        blank=True,
        null=True,
        verbose_name=_("Post Overview"),
    )
    # 内容
    content: models.TextField = models.TextField(
        blank=True,
        null=True,
        verbose_name=_("Post Content"),
    )
    # カテゴリー
    category: models.ForeignKey = models.ForeignKey(
        Categories,
        blank=True,
        null=True,
        on_delete=models.PROTECT,
        verbose_name=_("Category"),
    )
    # シリーズ
    series: models.ManyToManyField = models.ManyToManyField(
        Series,
        through="PostSeriesRel",
    )
    # タグ
    tags: models.ManyToManyField = models.ManyToManyField(
        Tags,
        through="PostTagRel",
    )

    def __str__(self) -> str:
        return str(self.title)
