from django.contrib.auth.models import User

from api.serializers.ob_serializer import OBSerializer


class UserSerializer(OBSerializer):
    """ユーザーシリアライザー．"""

    class Meta:
        model = User
        fields = [
            # 名前
            "first_name",
            # 苗字
            "last_name",
            # メールアドレス
            "email",
        ]
