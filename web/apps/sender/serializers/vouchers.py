from rest_framework import serializers

from apps.notification_user.models import UserConnectionField
from apps.sender.serializers import BaseSerializer


class NewFundSerializer(BaseSerializer):

    fund_name = serializers.CharField()
    username = serializers.CharField()

    def get_template(self):
        return '/vouchers/new_fund'
