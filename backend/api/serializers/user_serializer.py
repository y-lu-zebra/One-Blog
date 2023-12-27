from django.contrib.auth.models import User

from api.serializers.ob_serializer import OBSerializer


class UserSerializer(OBSerializer):
    """
    ユーザーシリアライザー
    """

    class Meta:
        model = User
        fields = [
            # 名
            "first_name",
            # 姓
            "last_name",
            # メールアドレス
            "email",
        ]
