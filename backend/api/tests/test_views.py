from django.contrib.auth.models import User
from parameterized import parameterized  # type: ignore
from rest_framework.test import APITestCase
from rest_framework.utils import json

from api.models import Categories, Posts, Series, Tags
from api.models.rels import PostSeriesRel, PostTagRel
from api.tests import data


class ViewSetTests(APITestCase):
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

        self.user = User.objects.create_superuser(**data.TEST_USERS_DATA[0])
        Categories.objects.bulk_create(
            self.__dict_to_model(data.TEST_CATEGORIES_DATA_LIST_1, Categories),
        )
        Categories.objects.bulk_create(
            self.__dict_to_model(data.TEST_CATEGORIES_DATA_LIST_2, Categories),
        )
        Series.objects.bulk_create(
            self.__dict_to_model(data.TEST_SERIES_DATA_LIST_1, Series),
        )
        Series.objects.bulk_create(
            self.__dict_to_model(data.TEST_SERIES_DATA_LIST_2, Series),
        )
        Tags.objects.bulk_create(
            self.__dict_to_model(data.TEST_TAGS_DATA_LIST, Tags),
        )
        Posts.objects.bulk_create(
            self.__dict_to_model(data.TEST_POSTS_DATA_LIST, Posts),
        )
        PostSeriesRel.objects.bulk_create(
            self.__dict_to_model(data.TEST_POST_SERIES_REL_LIST, PostSeriesRel, False),
        )
        PostTagRel.objects.bulk_create(
            self.__dict_to_model(data.TEST_POST_TAG_REL_LIST, PostTagRel, False),
        )

    def __dict_to_model(
        self,
        test_data: list,
        model,
        needs_user: bool = True,
    ) -> list:
        """
        辞書からモデルに変換する。

        Parameters
        ----------
        test_data   変換元のデータ
        model       変換先のモデルクラス
        needs_user  ユーザー情報必要フラグ（デフォルト値：True）

        Returns
        -------
            モデルに変換済みのオブジェクトのリスト
        """

        if needs_user:
            user_info = {"user_created": self.user, "user_updated": self.user}
        else:
            user_info = {}

        return list(map(lambda item: model(**user_info, **item), test_data))

    @parameterized.expand(
        [
            (
                "categories order, published and page 1",
                "/categories/",
                "name",
                200,
                7,
                [
                    data.TEST_CATEGORIES_DATA_LIST_1[2]["name"],
                    data.TEST_CATEGORIES_DATA_LIST_2[1]["name"],
                    data.TEST_CATEGORIES_DATA_LIST_1[6]["name"],
                    data.TEST_CATEGORIES_DATA_LIST_1[1]["name"],
                    data.TEST_CATEGORIES_DATA_LIST_1[4]["name"],
                ],
            ),
            (
                "categories order, published and page 2",
                "/categories/?offset=5",
                "name",
                200,
                7,
                [
                    data.TEST_CATEGORIES_DATA_LIST_1[5]["name"],
                    data.TEST_CATEGORIES_DATA_LIST_1[0]["name"],
                ],
            ),
            (
                "categories search name",
                "/categories/?name=キー",
                "name",
                200,
                2,
                [
                    data.TEST_CATEGORIES_DATA_LIST_1[2]["name"],
                    data.TEST_CATEGORIES_DATA_LIST_1[6]["name"],
                ],
            ),
            (
                "categories search type",
                "/categories/?type=EXT",
                "name",
                200,
                2,
                [
                    data.TEST_CATEGORIES_DATA_LIST_1[6]["name"],
                    data.TEST_CATEGORIES_DATA_LIST_1[5]["name"],
                ],
            ),
            (
                "categories search parent",
                "/categories/?parent=1",
                "name",
                200,
                1,
                [
                    data.TEST_CATEGORIES_DATA_LIST_2[1]["name"],
                ],
            ),
            (
                "categories search multiple conditions",
                "/categories/?name=その９&type=CAT&parent=1",
                "name",
                200,
                1,
                [
                    data.TEST_CATEGORIES_DATA_LIST_2[1]["name"],
                ],
            ),
            (
                "series order, published and page 1",
                "/series/",
                "name",
                200,
                6,
                [
                    data.TEST_SERIES_DATA_LIST_2[0]["name"],
                    data.TEST_SERIES_DATA_LIST_1[0]["name"],
                    data.TEST_SERIES_DATA_LIST_1[6]["name"],
                    data.TEST_SERIES_DATA_LIST_1[4]["name"],
                    data.TEST_SERIES_DATA_LIST_1[5]["name"],
                ],
            ),
            (
                "series order, published and page 2",
                "/series/?offset=5",
                "name",
                200,
                6,
                [
                    data.TEST_SERIES_DATA_LIST_1[1]["name"],
                ],
            ),
            (
                "tags order, published and page 1",
                "/tags/",
                "name",
                200,
                5,
                [
                    data.TEST_TAGS_DATA_LIST[0]["name"],
                    data.TEST_TAGS_DATA_LIST[4]["name"],
                    data.TEST_TAGS_DATA_LIST[5]["name"],
                    data.TEST_TAGS_DATA_LIST[2]["name"],
                    data.TEST_TAGS_DATA_LIST[1]["name"],
                ],
            ),
            (
                "posts order, published and page 1",
                "/posts/",
                "title",
                200,
                6,
                [
                    data.TEST_POSTS_DATA_LIST[5]["title"],
                    data.TEST_POSTS_DATA_LIST[3]["title"],
                    data.TEST_POSTS_DATA_LIST[6]["title"],
                    data.TEST_POSTS_DATA_LIST[2]["title"],
                    data.TEST_POSTS_DATA_LIST[0]["title"],
                ],
            ),
            (
                "posts order, published and page 2",
                "/posts/?offset=5",
                "title",
                200,
                6,
                [
                    data.TEST_POSTS_DATA_LIST[1]["title"],
                ],
            ),
        ]
    )
    def test_get(
        self,
        _: str,
        url: str,
        field_key: str,
        excepted_status: int,
        excepted_count: int,
        excepted_content,
    ) -> None:
        """
        一覧取得 API ビューのテスト

        Parameters
        ----------
        _                   実行時一覧表示用のパターン名
        url                 対象 API の URL
        field_key           検証用のフィールドのキー
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
            [item[field_key] for item in content["results"]],
            excepted_content,
            "結果データ",
        )
