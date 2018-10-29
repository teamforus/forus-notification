from rest_framework import serializers

from apps.sender.serializers import BaseEmailSerializer


class LoginViaEmailSerializer(BaseEmailSerializer):
    link = serializers.CharField()
    platform = serializers.CharField()

    def get_template(self):
        return '/login/login_via_emails'
