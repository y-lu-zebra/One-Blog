from django.contrib.auth.models import User
from django.test import TestCase
from parameterized import parameterized  # type: ignore

from api.models import Categories, Posts, Series, Tags
from api.models.rels import PostSeriesRel, PostTagRel
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

        self.user = User.objects.create_superuser(**data.TEST_USERS_DATA[0])
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
        self.tags = Tags.objects.create(
            user_created=self.user,
            user_updated=self.user,
            **data.TEST_TAGS_DATA_LIST[0],
        )
        self.posts = Posts.objects.create(
            user_created=self.user,
            user_updated=self.user,
            **data.TEST_POSTS_DATA_LIST[0],
        )
        self.post_tag_rel = PostTagRel.objects.create(
            post=self.posts,
            tag=self.tags,
        )
        self.post_series_rel = PostSeriesRel.objects.create(
            post=self.posts,
            series=self.series,
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
                + data.TEST_SERIES_DATA_LIST[0]["name"],
                "「投稿・シリーズ」リレーション（中間）モデルの文字列変換",
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

        Parameters
        ----------
        _           実行時一覧表示用のパターン名
        model       モデルクラス
        excepted    期待値
        msg         説明メッセージ

        Returns
        -------
            なし
        """

        model_obj: Categories | Series | Tags
        if model == "Categories":
            model_obj = self.category
        elif model == "Series":
            model_obj = self.series
        elif model == "Tags":
            model_obj = self.tags
        elif model == "Posts":
            model_obj = self.posts
        elif model == "PostTagRel":
            model_obj = self.post_tag_rel
        else:
            model_obj = self.post_series_rel

        self.assertEqual(str(model_obj), excepted, msg)
