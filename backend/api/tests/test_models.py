from typing import Any

from django.test import TestCase
from parameterized import parameterized  # type: ignore

from api.models import Categories, Posts, Series, Tags
from api.models.rels import PostSeriesRel, PostTagRel
from api.tests import data
from api.tests.functions import init_data


class ModelsTests(TestCase):
    """カテゴリーモデルのテストケース．"""

    def setUp(self) -> None:
        """前処理 本テストケースで使用するテストデータを作成しておく．

        Returns
        -------
            なし
        """

        init_data()

    @parameterized.expand(
        [
            (
                "Categories.__str__()",
                "Categories",
                data.TEST_CATEGORIES_DATA_LIST_1[0]["name"],
                "カテゴリーモデルの文字列変換",
            ),
            (
                "Series.__str__()",
                "Series",
                data.TEST_SERIES_DATA_LIST_1[0]["name"],
                "シリーズモデルの文字列変換",
            ),
            (
                "Tags.__str__()",
                "Tags",
                data.TEST_TAGS_DATA_LIST[0]["name"],
                "タグモデルの文字列変換",
            ),
            (
                "Posts.__str__()",
                "Posts",
                data.TEST_POSTS_DATA_LIST[0]["title"],
                "投稿モデルの文字列変換",
            ),
            (
                "PostTagRel.__str__()",
                "PostTagRel",
                data.TEST_POSTS_DATA_LIST[0]["title"]
                + "-"
                + data.TEST_TAGS_DATA_LIST[0]["name"],
                "「投稿・タグ」リレーション（中間）モデルの文字列変換",
            ),
            (
                "PostSeriesRel.__str__()",
                "PostSeriesRel",
                data.TEST_POSTS_DATA_LIST[0]["title"]
                + "-"
                + data.TEST_SERIES_DATA_LIST_1[0]["name"],
                "「投稿・シリーズ」リレーション（中間）モデルの文字列変換",
            ),
        ]
    )
    def test_str(
        self,
        _: str,
        model: Any,
        excepted: Any,
        msg: str,
    ) -> None:
        """モデルのメソッド __str__ のテスト．

        Parameters
        ----------
        _ : str
            実行時一覧表示用のパターン名
        model: Any
            モデルクラス
        excepted : Any
            期待値
        msg : str
            説明メッセージ

        Returns
        -------
            なし
        """

        model_obj: Categories | Series | Tags | Posts | PostTagRel | PostSeriesRel
        if model == "Categories":
            model_obj = Categories.objects.get(pk=1)
        elif model == "Series":
            model_obj = Series.objects.get(pk=1)
        elif model == "Tags":
            model_obj = Tags.objects.get(pk=1)
        elif model == "Posts":
            model_obj = Posts.objects.get(pk=1)
        elif model == "PostTagRel":
            model_obj = PostTagRel.objects.get(pk=1)
        else:
            model_obj = PostSeriesRel.objects.get(pk=1)

        self.assertEqual(str(model_obj), excepted, msg)
