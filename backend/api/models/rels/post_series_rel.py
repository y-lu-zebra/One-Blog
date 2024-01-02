from django.apps import apps
from django.db import models
from django.utils.translation import gettext_lazy as _

from api.models.posts import Posts
from api.models.series import Series
from backend.commons import constants


class PostSeriesRel(models.Model):
    """
    「投稿・シリーズ」リレーション（中間）モデル
    """

    class Meta:
        db_table = constants.CODE_SEP_UNDERSCORE.join(
            [apps.get_app_config("api").name, "post_series_rel"]
        )
        verbose_name = verbose_name_plural = _("Post Series Relationship")
        unique_together = ("post", "series")

    # 投稿
    post: models.ForeignKey = models.ForeignKey(
        Posts,
        on_delete=models.PROTECT,
        verbose_name=_("Posts"),
    )
    # シリーズ
    series: models.ForeignKey = models.ForeignKey(
        Series,
        on_delete=models.PROTECT,
        verbose_name=_("Series"),
    )

    def __str__(self) -> str:
        return f"{self.post}-{self.series}"
