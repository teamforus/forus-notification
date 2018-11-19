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


class SmsNotificationSerializer(serializers.Serializer):
    title = serializers.CharField()
    phone = serializers.CharField()

    def validate(self, attrs):
        super(SmsNotificationSerializer, self).validate(attrs)
        self.title = attrs['title']
        self.phone = attrs['phone']
        return attrs
