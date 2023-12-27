from django.apps import apps
from django.db import models
from django.utils.translation import gettext_lazy as _

from api.models.mixins import CreatedMixin, LinkMixin, SEOMixin, UpdatedMixin
from backend.commons import constants


class Categories(LinkMixin, SEOMixin, CreatedMixin, UpdatedMixin):
    """
    カテゴリーモデル
    """

    # カテゴリータイプの選択肢
    TYPE_CHOICES = [
        ("CAT", _("Category")),
        ("SGL", _("Single Page")),
        ("EXT", _("External Page")),
    ]

    class Meta:
        db_table = constants.CODE_SEP_UNDERSCORE.join(
            [apps.get_app_config("api").name, "categories"]
        )
        verbose_name = verbose_name_plural = _("Categories")

    # カテゴリー名
    name: models.CharField = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        verbose_name=_("Category Name"),
    )
    # タイプ
    type: models.CharField = models.CharField(
        max_length=3,
        blank=False,
        null=False,
        default=TYPE_CHOICES[0][0],
        choices=TYPE_CHOICES,
        verbose_name=_("Category Type"),
    )
    # 親カテゴリー
    parent: models.ForeignKey = models.ForeignKey(
        "self",
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        verbose_name=_("Parent Category"),
    )

    def __str__(self) -> str:
        return str(self.name)
