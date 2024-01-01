from django.contrib.auth.models import User

from api.models import Categories, Posts, Series, Tags
from api.models.rels import PostSeriesRel, PostTagRel
from api.tests import data


def init_data() -> None:
    """
    試験データ作成

    Returns
    -------
        なし
    """

    user = User.objects.create_superuser(**data.TEST_USERS_DATA[0])
    category = Categories.objects.create(
        user_created=user,
        user_updated=user,
        **data.TEST_CATEGORIES_DATA_LIST_1[0],
    )
    series = Series.objects.create(
        user_created=user,
        user_updated=user,
        **data.TEST_SERIES_DATA_LIST_1[0],
    )
    tags = Tags.objects.create(
        user_created=user,
        user_updated=user,
        **data.TEST_TAGS_DATA_LIST[0],
    )
    posts = Posts.objects.create(
        user_created=user,
        user_updated=user,
        **data.TEST_POSTS_DATA_LIST[0],
        category=category,
    )
    PostTagRel.objects.create(
        post=posts,
        tag=tags,
    )
    PostSeriesRel.objects.create(
        post=posts,
        series=series,
    )
