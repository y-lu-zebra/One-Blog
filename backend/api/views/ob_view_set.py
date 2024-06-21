import logging

from rest_framework import viewsets


class OBViewSet(viewsets.ReadOnlyModelViewSet):
    """基底ビューセット．"""

    # ロガー
    logger = logging.getLogger("django")

    def perform_create(self, serializer):
        """新規作成 API が呼び出された際に，作成者と最終更新者を自動追加する．

        Parameters
        ----------
        serializer
            シリアライザー

        Returns
        -------
            なし
        """

        serializer.save(user_created=self.request.user, user_updated=self.request.user)

    def perform_update(self, serializer):
        """更新 API が呼び出された際に，最終更新者を自動更新する．

        Parameters
        ----------
        serializer
            シリアライザー

        Returns
        -------
            なし
        """

        serializer.save(user_updated=self.request.user)
