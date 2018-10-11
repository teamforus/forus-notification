from rest_framework import serializers

from apps.notification_user.models import UserConnectionField


class SenderSerializer(serializers.Serializer):


    def validate(self, attrs):
        return attrs
