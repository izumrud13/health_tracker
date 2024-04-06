from rest_framework import serializers

from users.models import User


class UserSerializers(serializers.ModelSerializer):
    """Сериалайзер для модели пользователя"""

    class Meta:
        model = User
        fields = '__all__'
