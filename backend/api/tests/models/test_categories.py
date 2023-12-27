from django.contrib.auth.models import User
from django.test import TestCase

from api.models import Categories
from api.tests import data


class CategoriesTests(TestCase):
    """
    カテゴリーモデルのテストケース
    """

    def setUp(self) -> None:
        """
        前処理
        本テストケースで使用するテストデータを作成しておく。

        Returns
        -------
            なし
        """

        self.user = User.objects.create_superuser(**data.TEST_USERS_DATA)
        self.category = Categories.objects.create(
            user_created=self.user,
            user_updated=self.user,
            **data.TEST_CATEGORIES_DATA_LIST[0],
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
            data.TEST_CATEGORIES_DATA_LIST[0]["name"],
            "文字列変換",
        )
