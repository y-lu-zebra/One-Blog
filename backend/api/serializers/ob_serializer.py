import logging

from rest_framework import serializers


class OBSerializer(serializers.ModelSerializer):
    """
    基底シリアライザー
    """

    # ロガー
    logger = logging.getLogger("django")
