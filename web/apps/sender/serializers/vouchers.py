from rest_framework import serializers

from apps.notification_user.models import UserConnectionField
from apps.sender.serializers import BaseSerializer


class NewFundSerializer(BaseSerializer):
    fund_name = serializers.CharField()
    username = serializers.CharField()

    def get_template(self):
        return '/vouchers/new_fund'



class ProviderApprovedSerializer(BaseSerializer):
    fund_name = serializers.CharField()
    provider_name = serializers.CharField()
    sponsor_name = serializers.CharField()
    date_start = serializers.DateField(format="%d-%m-%Y")

    def get_template(self):
        return '/vouchers/provider_approved'


class ProviderAppliedSerializer(BaseSerializer):
    fund_name = serializers.CharField()
    provider_name = serializers.CharField()
    sponsor_name = serializers.CharField()

    def get_template(self):
        return '/vouchers/provider_applied'


class NewProductAddedSerializer(BaseSerializer):
    product_name = serializers.CharField()
    provider_name = serializers.CharField()

    def get_template(self):
        return '/vouchers/new_product_added'
