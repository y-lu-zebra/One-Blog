from django.contrib import admin

from api.models.rels import PostTagRel


class PostTagRelInline(admin.TabularInline):
    """「投稿・タグ」リレーション（中間）インラインクラス．"""

    model = PostTagRel
    extra = 1
