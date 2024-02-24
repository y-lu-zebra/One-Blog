import os
import shutil

from django.test import TestCase
from parameterized import parameterized  # type: ignore

from backend.utils import files


class FilesTests(TestCase):
    """
    ファイル操作ユーティリティ関数のテストケース
    """

    # カレントディレクトリ
    CUR_DIR = os.path.dirname(__file__)
    # テストデータを保存用の一時フォルダーのパス
    TMP_DIR = os.path.join(CUR_DIR, "tmp")
    # 存在しないフォルダーのパス
    NOT_EXISTS_DIR = os.path.join(TMP_DIR, "not_exists")
    # 再帰的に作成するためのフォルダーのパス
    RECURSION_DIR = os.path.join(TMP_DIR, "level_1", "level_2")

    def setUp(self) -> None:
        """
        前処理
        本テストケースで使用するディレクトリ・ファイルを事前に準備する。

        Returns
        -------
            なし
        """

        # テストファイル格納用の一時ディレクトリを作成
        if not os.path.exists(self.TMP_DIR):
            os.makedirs(self.TMP_DIR)

    def tearDown(self) -> None:
        """
        後処理
        本テストケースで使用したディレクトリ・ファイルのゴミを片付ける。

        Returns
        -------
            なし
        """

        # テストファイル格納用の一時ディレクトリを丸ごと削除
        if os.path.isdir(self.TMP_DIR):
            shutil.rmtree(self.TMP_DIR)

    @parameterized.expand(
        [
            (
                "existed",
                TMP_DIR,
                True,
                "存在したパスを指定",
            ),
            (
                "not existed",
                NOT_EXISTS_DIR,
                False,
                "存在しないパスを指定",
            ),
        ]
    )
    def test_is_path_exists(
        self,
        _: str,
        path: str,
        excepted: bool,
        msg: str,
    ) -> None:
        """
        関数 is_path_exists のテスト

        Parameters
        ----------
        _           実行時一覧表示用のパターン名
        path        チェックしたいパスの文字列
        excepted    チェック結果の期待値
        msg         説明メッセージ

        Returns
        -------
            なし
        """

        # 試験対象を呼び出し
        rst = files.is_path_exists(path)

        # 試験結果を確認
        self.assertIs(rst, excepted, msg)

    @parameterized.expand(
        [
            (
                "existed",
                TMP_DIR,
                True,
                True,
                "存在したフォルダーを指定",
            ),
            (
                "not existed",
                NOT_EXISTS_DIR,
                False,
                True,
                "存在しないフォルダーを指定",
            ),
            (
                "recursion",
                RECURSION_DIR,
                False,
                True,
                "再帰的に作成",
            ),
        ]
    )
    def test_make_dir(
        self,
        _: str,
        path: str,
        excepted_before: bool,
        excepted_after: bool,
        msg: str,
    ) -> None:
        """
        関数 make_dir のテスト

        Parameters
        ----------
        _               実行時一覧表示用のパターン名
        path            作成したいディレクトリの絶対パス
        excepted_before テストを行う前の期待値
        excepted_after  テストを行う後の期待値
        msg             説明メッセージ

        Returns
        -------
            なし
        """

        # テスト対象を呼び出す前の確認
        self.assertIs(os.path.exists(path), excepted_before, msg)
        # 試験対象を呼び出し
        files.make_dir(path)
        # 試験結果を確認
        self.assertIs(os.path.exists(path), excepted_after, msg)
