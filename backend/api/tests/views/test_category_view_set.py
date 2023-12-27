from django.contrib.auth.models import User
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

    def test_get(self) -> None:
        """
        カテゴリー一覧取得 API ビューのテスト

        Returns
        -------
            なし
        """

        # 試験対象を呼び出し
        res = self.client.get("/categories/")

        content = json.loads(res.content)

        # 試験結果を確認
        self.assertEqual(
            res.status_code,
            200,
            "レスポンスステータス",
        )
        self.assertEqual(
            content["count"],
            len(data.TEST_CATEGORIES_DATA_LIST),
            "データ数",
        )
        self.assertEqual(
            [cat["name"] for cat in content["results"]],
            [
                "テストカテゴリーその２",
                "テストカテゴリーその３",
                "テストカテゴリーその１",
            ],
            "並び順",
        )
