import os
from pathlib import Path

"""
ファイル・ディレクトリ関連
"""
# 設定ファイル（本番用）の名称
FILE_ENV = ".env"
# 設定ファイル（テスト用）の名称
FILE_ENV_TEST = ".env.test"

# 基礎 APP のフォルダ名
DIR_APP_BASE = "backend"
# 静的ファイルのフォルダ名
DIR_STATIC = "static"

# プロジェクトのルートパス
PATH_PROJECT = str(Path(__file__).resolve().parent.parent.parent.parent)
# バックエンドのルートパス
PATH_BACKEND = str(Path(__file__).resolve().parent.parent.parent)
# 設定ファイル（本番用）の絶対パス
PATH_ENV = os.path.join(PATH_PROJECT, FILE_ENV)
# 設定ファイル（テスト用）の絶対パス
PATH_ENV_TEST = os.path.join(PATH_PROJECT, FILE_ENV_TEST)
# 静的ファイルのフォルダの絶対パス
PATH_STATIC = os.path.join(PATH_BACKEND, DIR_APP_BASE, DIR_STATIC)

"""
各種コード関連
"""
# 単体テストモードの文字列
CODE_MODE_TEST = "test"
