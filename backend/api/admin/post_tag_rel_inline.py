from django.contrib import admin

from api.models.rels import PostTagRel


class PostTagRelInline(admin.TabularInline):
    model = PostTagRel
    extra = 1
