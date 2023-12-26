from django.apps import apps
from django.db import models
from django.utils.translation import gettext_lazy as _

from api.models.mixins import CreatedMixin
from api.models.posts import Posts
from api.models.tags import Tags
from backend.commons import constants


class PostTagRel(CreatedMixin):
    """
    「投稿・タグ」リレーションモデル
    """

    class Meta:
        db_table = constants.CODE_SEP_UNDERSCORE.join(
            [apps.get_app_config("api").name, "post_tag_rel"]
        )
        verbose_name = verbose_name_plural = _("Post Tag Relationship")

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
