from typing import Any
from unittest.mock import Mock

from django.contrib.admin import AdminSite
from django.contrib.auth.models import User
from django.test import TestCase
from parameterized import parameterized  # type: ignore

from api.admin.ob_admin import OBAdmin
from api.models import Categories, Series, Tags
from api.tests import data


class AdminTests(TestCase):
    """
    ADMIN のテストケース
    """

    def setUp(self) -> None:
        """
        前処理
        本テストケースで使用するテストデータを作成しておく。

        Returns
        -------
            なし
        """

        self.site = AdminSite()
        self.user = User.objects.create_superuser(**data.TEST_USERS_DATA)

    @parameterized.expand(
        [
            (
                "CategoryAdmin.save_model()",
                Categories,
                data.TEST_CATEGORIES_DATA_LIST[0],
            ),
            (
                "SeriesAdmin.save_model()",
                Series,
                data.TEST_SERIES_DATA_LIST[0],
            ),
            (
                "TagAdmin.save_model()",
                Tags,
                data.TEST_TAGS_DATA_LIST[0],
            ),
        ]
    )
    def test_save_model(
        self,
        _: str,
        model: Any,
        test_data: dict,
    ) -> None:
        """
        OBAdmin のメソッド save_model のテスト

        Parameters
        ----------
        _           実行時一覧表示用のパターン名
        model       モデルクラス
        test_data   テストデータ

        Returns
        -------

        """

        oba = OBAdmin(model, self.site)
        # 試験対象を呼び出し
        oba.save_model(
            request=Mock(user=self.user),
            instance=model(**test_data),
            form=None,
            change=None,
        )

        # 試験結果を確認
        cat: model = model.objects.get(pk=1)
        self.assertEqual(cat.user_created, self.user, "作成者")
        self.assertEqual(cat.user_updated, self.user, "最終更新者")
