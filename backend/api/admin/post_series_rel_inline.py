from django.contrib import admin

from api.models.rels import PostSeriesRel


class PostSeriesRelInline(admin.TabularInline):
    model = PostSeriesRel
    extra = 1
