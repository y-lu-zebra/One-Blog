from typing import Any

from rest_framework.response import Response
from rest_framework.views import exception_handler


def one_exception_handler(exc: Exception, context: dict[str, Any]) -> Response:
    """基本例外ハンドラー．

    Parameters
    ----------
    exc
    context

    Returns
    -------
        異常時利用するレスポンス．
    """

    response = exception_handler(exc, context)

    if response is not None:
        response.data = {"messages": response.data, "code": "E310998"}
    else:
        response = Response()

    return response
