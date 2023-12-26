from django.contrib.auth.models import User
from django.test import TestCase

from api.models import Categories


class CategoriesTests(TestCase):
    """
    カテゴリーモデルのテストケース
    """

    # ユーザーのテストデータ
    TEST_USERS_DATA = {
        "email": "test@test.test",
        "password": "<PASSWORD>",
    }
    # カテゴリーのテストデータ
    TEST_CATEGORIES_DATA = {
        "name": "テストカテゴリーその１",
        "type": "CAT",
    }

    def setUp(self) -> None:
        """
        前処理
        本テストケースで使用するテストデータを作成しておく。

        Returns
        -------
            なし
        """

        self.user = User.objects.create(**self.TEST_USERS_DATA)
        self.category = Categories.objects.create(
            created_user=self.user,
            updated_user=self.user,
            **self.TEST_CATEGORIES_DATA,
        )

    def test_str(self) -> None:
        """
        メソッド __str__ のテスト

        Returns
        -------
            なし
        """

        self.assertEqual(
            str(self.category),
            self.TEST_CATEGORIES_DATA["name"],
            "文字列変換",
        )
