from django.contrib import admin

from api.models.rels import PostSeriesRel


class PostSeriesRelInline(admin.TabularInline):
    """「投稿・シリーズ」リレーション（中間）インラインクラス．"""

    model = PostSeriesRel
    extra = 1
