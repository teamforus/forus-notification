from rest_framework import serializers

from apps.notification_user.models import UserConnectionField


class UserConnectionFieldSerializer(serializers.Serializer):

    user_id = serializers.Serializer()

    class Meta:
        model = UserConnectionField
        fields = ('user_id', 'value', 'type')
