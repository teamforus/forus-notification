from rest_framework import serializers

from apps.notification_user.models import UserConnectionField


class UserConnectionFieldSerializer(serializers.Serializer):
    user_id = serializers.CharField()
    value = serializers.CharField()
    type = serializers.IntegerField()

    def validate(self, attrs):
        self.user_id = attrs['user_id']
        self.value = attrs['value']
        self.type = attrs['type']
        return attrs



class RemoveUserConnectionFieldSerializer(serializers.Serializer):
    value = serializers.CharField()

    def validate(self, attrs):
        self.value = attrs['value']
        return attrs
