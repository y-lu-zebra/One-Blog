from django.contrib.auth.models import User
from parameterized import parameterized  # type: ignore
from rest_framework.test import APITestCase
from rest_framework.utils import json

from api.models import Categories
from api.tests import data


class CategoryViewSetTests(APITestCase):
    """
    カテゴリービューセットのテストケース
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
        categories: list[Categories] = list(
            map(
                lambda cat: Categories(
                    user_created=self.user, user_updated=self.user, **cat
                ),
                data.TEST_CATEGORIES_DATA_LIST,
            )
        )
        Categories.objects.bulk_create(categories)

    @parameterized.expand(
        [
            (
                "order",
                "/categories/",
                200,
                len(data.TEST_CATEGORIES_DATA_LIST),
                [
                    data.TEST_CATEGORIES_DATA_LIST[1]["name"],
                    data.TEST_CATEGORIES_DATA_LIST[2]["name"],
                    data.TEST_CATEGORIES_DATA_LIST[0]["name"],
                ],
            ),
            (
                "name filter",
                "/categories/?name=カテゴリー",
                200,
                2,
                [
                    data.TEST_CATEGORIES_DATA_LIST[2]["name"],
                    data.TEST_CATEGORIES_DATA_LIST[0]["name"],
                ],
            ),
            (
                "type filter",
                "/categories/?type=SGL",
                200,
                1,
                [
                    data.TEST_CATEGORIES_DATA_LIST[1]["name"],
                ],
            ),
            (
                "all filters",
                "/categories/?type=CAT&name=その３",
                200,
                1,
                [
                    data.TEST_CATEGORIES_DATA_LIST[2]["name"],
                ],
            ),
        ]
    )
    def test_get(
        self,
        _: str,
        url: str,
        excepted_status: int,
        excepted_count: int,
        excepted_content,
    ) -> None:
        """
        カテゴリー一覧取得 API ビューのテスト

        Parameters
        ----------
        _                   実行時一覧表示用のパターン名
        url                 対象 API の　URL
        excepted_status     レスポンスステータスの期待値
        excepted_count      一致したデータ数の期待値
        excepted_content    結果データの期待値

        Returns
        -------
            なし

        """

        # 試験対象を呼び出し
        res = self.client.get(url)

        content = json.loads(res.content)

        # 試験結果を確認
        self.assertEqual(
            res.status_code,
            excepted_status,
            "レスポンスステータス",
        )
        self.assertEqual(
            content["count"],
            excepted_count,
            "データ数",
        )
        self.assertEqual(
            [cat["name"] for cat in content["results"]],
            excepted_content,
            "結果データ",
        )
