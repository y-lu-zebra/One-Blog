#!/usr/bin/env python
"""Django タスク管理用のコマンドラインツール．"""

import os
import sys


def main() -> None:
    """管理タスクを実行する．"""

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "one.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError("Failed to import Django!") from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
