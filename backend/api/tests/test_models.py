from django.contrib.auth.models import User
from django.test import TestCase
from parameterized import parameterized  # type: ignore

from api.models import Categories, Series
from api.tests import data


class ModelsTests(TestCase):
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
        self.series = Series.objects.create(
            user_created=self.user,
            user_updated=self.user,
            **data.TEST_SERIES_DATA_LIST[0],
        )

    @parameterized.expand(
        [
            (
                "Categories.__str__()",
                "Categories",
                data.TEST_CATEGORIES_DATA_LIST[0]["name"],
                "カテゴリーモデルの文字列変換",
            ),
            (
                "Series.__str__()",
                "Series",
                data.TEST_SERIES_DATA_LIST[0]["name"],
                "シリーズモデルの文字列変換",
            ),
        ]
    )
    def test_str(
        self,
        _: str,
        model: str,
        excepted: str,
        msg: str,
    ) -> None:
        """
        モデルのメソッド __str__ のテスト

        Returns
        -------
            なし
        """

        model_obj: Categories | Series
        if model == "Categories":
            model_obj = self.category
        else:
            model_obj = self.series

        self.assertEqual(str(model_obj), excepted, msg)
