# ユーザーのテストデータ
TEST_USERS_DATA = {
    "username": "test",
    "email": "test@test.test",
    "password": "test",
}
# カテゴリーのテストデータ
TEST_CATEGORIES_DATA_LIST: list[dict] = [
    {
        "name": "テストカテゴリーその１",
        "type": "CAT",
    },
    {
        "name": "テストシングルページその２",
        "type": "SGL",
        "sort_order": 3,
    },
    {
        "name": "テストカテゴリーその３",
        "type": "CAT",
        "sort_order": 2,
    },
]
# シリーズのテストデータ
TEST_SERIES_DATA_LIST: list[dict] = [
    {
        "name": "テストシリーズその１",
        "sort_order": 1,
    },
    {
        "name": "テストシリーズその２",
    },
    {
        "name": "テストシリーズその３",
        "sort_order": 2,
    },
]
