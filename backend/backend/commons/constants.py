"""
バックエンドの定数定義
"""
import os
from pathlib import Path

"""
アプリ設定
"""
# アプリバージョン
VERSION = "0.1.0"

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
# 翻訳ファイルのフォルダ名
DIR_LOCALE = "locale"
# テンプレートのフォルダ名
DIR_TEMPLATE = "templates"

# プロジェクトのルートパス
PATH_PROJECT = str(Path(__file__).resolve().parent.parent.parent.parent)
# バックエンドのルートパス
PATH_BACKEND = str(Path(__file__).resolve().parent.parent.parent)
# 設定ファイル（本番用）の絶対パス
PATH_ENV = os.path.join(PATH_PROJECT, FILE_ENV)
# 設定ファイル（テスト用）の絶対パス
PATH_ENV_TEST = os.path.join(PATH_PROJECT, FILE_ENV_TEST)
# 静的ファイルのフォルダの絶対パス
PATH_STATIC_LIST = [os.path.join(PATH_BACKEND, "admin_theme", DIR_STATIC)]
# 翻訳ファイルのフォルダの絶対パス
PATH_LOCALE = os.path.join(PATH_BACKEND, DIR_LOCALE)
# テンプレートのフォルダの絶対パス
PATH_TEMPLATE_LIST = [os.path.join(PATH_BACKEND, "admin_theme", DIR_TEMPLATE)]

"""
各種コード関連
"""
# 単体テストモードの文字列
CODE_MODE_TEST = "test"
# OS セパレータ
CODE_SEP_OS = os.sep
# アンダースコア セパレータ
CODE_SEP_UNDERSCORE = "_"
# URL セパレータ
CODE_SEP_URL = "/"
# ログファイル拡張子
CODE_EXT_LOG = ".log"

# バイト - メガ 換算
HEX_BYTE = 1024 * 1024
