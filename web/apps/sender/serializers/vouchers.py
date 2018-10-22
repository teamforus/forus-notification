from rest_framework import serializers

from apps.notification_user.models import UserConnectionField
from apps.sender.serializers import BaseEmailSerializer


class NewFundEmailSerializer(BaseEmailSerializer):
    fund_name = serializers.CharField()
    username = serializers.CharField()

    def get_template(self):
        return '/vouchers/new_fund'


class NewFundCreatedEmailSerializer(BaseEmailSerializer):
    fund_name = serializers.CharField()
    requester_name = serializers.CharField()
    link = serializers.CharField()

    def get_template(self):
        return '/vouchers/new_fund_created'


class ProviderApprovedEmailSerializer(BaseEmailSerializer):
    fund_name = serializers.CharField()
    provider_name = serializers.CharField()
    sponsor_name = serializers.CharField()
    date_start = serializers.DateField(format="%d-%m-%Y")

    def get_template(self):
        return '/vouchers/provider_approved'


class ProviderAppliedEmailSerializer(BaseEmailSerializer):
    fund_name = serializers.CharField()
    provider_name = serializers.CharField()
    sponsor_name = serializers.CharField()

    def get_template(self):
        return '/vouchers/provider_applied'


class NewProductAddedEmailSerializer(BaseEmailSerializer):
    product_name = serializers.CharField()
    provider_name = serializers.CharField()

    def get_template(self):
        return '/vouchers/new_product_added'



class ProviderRejectedSerializer(BaseEmailSerializer):
    product_name = serializers.CharField()
    sponsor_name = serializers.CharField()
    provider_name = serializers.CharField()
    fund_name = serializers.CharField()

    def get_template(self):
        return '/vouchers/provider_rejected'