from django.apps import apps
from django.db import models
from django.utils.translation import gettext_lazy as _

from api.models.categories import Categories
from api.models.mixins import CreatedMixin, LinkMixin, SEOMixin, UpdatedMixin
from api.models.series import Series
from api.models.tags import Tags
from backend.commons import constants


class Posts(LinkMixin, SEOMixin, CreatedMixin, UpdatedMixin):
    """
    投稿モデル
    """

    class Meta:
        db_table = constants.CODE_SEP_UNDERSCORE.join(
            [apps.get_app_config("api").name, "posts"]
        )
        verbose_name = verbose_name_plural = _("Posts")

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
        related_name="post_%(class)s_set",
        verbose_name=_("Category"),
    )
    # シリーズ
    series: models.ForeignKey = models.ForeignKey(
        Series,
        blank=True,
        null=True,
        on_delete=models.PROTECT,
        related_name="post_%(class)s_set",
        verbose_name=_("Series"),
    )
    # タグ
    tags: models.ManyToManyField = models.ManyToManyField(
        Tags,
        through="PostTagRel",
        related_name="posts",
    )

    def __str__(self) -> str:
        return str(self.title)
