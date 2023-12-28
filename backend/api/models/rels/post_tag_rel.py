from django.apps import apps
from django.db import models
from django.utils.translation import gettext_lazy as _

from api.models.posts import Posts
from api.models.tags import Tags
from backend.commons import constants


class PostTagRel(models.Model):
    """
    「投稿・タグ」リレーション（中間）モデル
    """

    class Meta:
        db_table = constants.CODE_SEP_UNDERSCORE.join(
            [apps.get_app_config("api").name, "post_tag_rel"]
        )
        verbose_name = verbose_name_plural = _("Post Tag Relationship")
        unique_together = ("post", "tag")

    # 投稿
    post: models.ForeignKey = models.ForeignKey(
        Posts,
        on_delete=models.PROTECT,
        verbose_name=_("Posts"),
    )
    # タグ
    tag: models.ForeignKey = models.ForeignKey(
        Tags,
        on_delete=models.PROTECT,
        verbose_name=_("Tags"),
    )

    def __str__(self) -> str:
        return f"{self.post}-{self.tag}"
