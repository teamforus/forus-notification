from rest_framework import serializers

from apps.sender.serializers import BaseMobileSerializer


class PushNotificationSerializer(BaseMobileSerializer):
    title = serializers.CharField()
    body = serializers.CharField()


    def validate(self, attrs):
        super(PushNotificationSerializer, self).validate(attrs)
        self.title = attrs['title']
        self.body = attrs['body']
        return attrs
