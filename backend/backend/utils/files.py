"""
ファイル操作ユーティリティ関数定義
"""
import os


def is_path_exists(path: str) -> bool:
    """
    指定されたパスが存在するかチェックする。

    Parameters
    ----------
    path
        チェックしたいパスの文字列
    Returns
    -------
        チェック結果
    """

    return os.path.exists(path)


def make_dir(path: str) -> None:
    """
    指定されたディレクトリが存在しない場合に、再帰的に作成する。

    Parameters
    ----------
    path
        作成したいディレクトリ
    Returns
    -------
        なし
    """

    if not is_path_exists(path):
        os.makedirs(path)
