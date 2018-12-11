from rest_framework import serializers

from apps.sender.serializers import BaseEmailSerializer


class EmailActivationSerializer(BaseEmailSerializer):
    link = serializers.CharField()
    platform = serializers.CharField()

    def get_template(self):
        return '/user/email_activation'
