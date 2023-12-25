import logging

from rest_framework import viewsets


class OBViewSet(viewsets.ModelViewSet):
    """
    基底ビューセット
    """

    # ロガー
    logger = logging.getLogger("django")
