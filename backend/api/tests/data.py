# ユーザーのテストデータ
TEST_USERS_DATA = [
    {
        "username": "test1",
        "email": "test1@test.test",
        "password": "test1",
    },
    {
        "username": "test2",
        "email": "test2@test.test",
        "password": "test2",
    },
]
# カテゴリーのテストデータその１
TEST_CATEGORIES_DATA_LIST_1: list[dict] = [
    {
        "name": "テストカテゴリーその１",
        "type": "CAT",
        "is_published": True,
    },
    {
        "name": "テストシングルページその２",
        "type": "SGL",
        "sort_order": 3,
        "is_published": True,
    },
    {
        "name": "テストカテゴリーその３キー",
        "type": "CAT",
        "sort_order": 7,
        "is_published": True,
    },
    {
        "name": "テストカテゴリーその４キー",
        "type": "CAT",
        "sort_order": 4,
        "is_published": False,
    },
    {
        "name": "テストカテゴリーその５",
        "type": "CAT",
        "sort_order": 1,
        "is_published": True,
    },
    {
        "name": "外部ページその６",
        "type": "EXT",
        "is_published": True,
    },
    {
        "name": "外部ページその７キー",
        "type": "EXT",
        "sort_order": 5,
        "is_published": True,
    },
]
# カテゴリーのテストデータその２
TEST_CATEGORIES_DATA_LIST_2: list[dict] = [
    {
        "name": "テストカテゴリーその８",
        "type": "CAT",
        "parent_id": 1,
    },
    {
        "name": "テストカテゴリーその９",
        "type": "CAT",
        "sort_order": 6,
        "is_published": True,
        "parent_id": 1,
    },
]
# シリーズのテストデータその１
TEST_SERIES_DATA_LIST_1: list[dict] = [
    {
        "name": "テストシリーズその１",
        "sort_order": 5,
        "is_published": True,
    },
    {
        "name": "テストシリーズその２",
        "is_published": True,
    },
    {
        "name": "テストシリーズその３",
        "sort_order": 2,
        "is_published": False,
    },
    {
        "name": "テストシリーズその４",
        "sort_order": 3,
    },
    {
        "name": "テストシリーズその５",
        "sort_order": 1,
        "is_published": True,
    },
    {
        "name": "テストシリーズその６",
        "is_published": True,
    },
    {
        "name": "テストシリーズその７",
        "sort_order": 4,
        "is_published": True,
    },
]
# シリーズのテストデータその２
TEST_SERIES_DATA_LIST_2: list[dict] = [
    {
        "name": "テストシリーズその8",
        "sort_order": 6,
        "is_published": True,
        "parent_id": 5,
    },
]
# タグのテストデータ
TEST_TAGS_DATA_LIST: list[dict] = [
    {
        "name": "タグその１",
        "sort_order": 5,
        "is_published": True,
    },
    {
        "name": "タグその２",
        "is_published": True,
    },
    {
        "name": "タグその３",
        "sort_order": 2,
        "is_published": True,
    },
    {
        "name": "タグその４",
        "sort_order": 1,
        "is_published": False,
    },
    {
        "name": "タグその５",
        "sort_order": 4,
        "is_published": True,
    },
    {
        "name": "タグその６",
        "sort_order": 3,
        "is_published": True,
    },
]
# 投稿のテストデータ
TEST_POSTS_DATA_LIST: list[dict] = [
    {
        "title": "投稿その１",
        "sort_order": 1,
        "is_published": True,
    },
    {
        "title": "投稿その２",
        "is_published": True,
        "category_id": 3,
    },
    {
        "title": "投稿その３",
        "sort_order": 2,
        "is_published": True,
    },
    {
        "title": "投稿その４",
        "sort_order": 3,
        "is_published": True,
    },
    {
        "title": "投稿その５",
        "sort_order": 1,
    },
    {
        "title": "投稿その６",
        "sort_order": 4,
        "is_published": True,
    },
    {
        "title": "投稿その７",
        "sort_order": 2,
        "is_published": True,
    },
    {
        "title": "投稿その８",
        "is_published": False,
    },
]
# 投稿-シリーズのテストデータ
TEST_POST_SERIES_REL_LIST: list[dict] = [
    {
        "post_id": 2,
        "series_id": 2,
    },
    {
        "post_id": 2,
        "series_id": 7,
    },
]
# 投稿-タグのテストデータ
TEST_POST_TAG_REL_LIST: list[dict] = [
    {
        "post_id": 2,
        "tag_id": 1,
    },
    {
        "post_id": 3,
        "tag_id": 1,
    },
    {
        "post_id": 3,
        "tag_id": 5,
    },
]
