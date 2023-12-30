from rest_framework import filters

from api.models import Posts
from api.serializers import PostSerializer
from api.views.ob_view_set import OBViewSet


class PostViewSet(OBViewSet):
    """
    投稿ビューセット
    """

    queryset = Posts.objects.filter(is_published=True).all()
    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["title", "overview", "content"]
