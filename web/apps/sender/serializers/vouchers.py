from rest_framework import serializers

from apps.notification_user.models import UserConnectionField
from apps.sender.serializers import BaseEmailSerializer


class NewFundEmailSerializer(BaseEmailSerializer):
    fund_name = serializers.CharField()
    provider_dashboard_link = serializers.CharField()

    def get_template(self):
        return '/vouchers/new_fund'


class NewFundCreatedEmailSerializer(BaseEmailSerializer):
    fund_name = serializers.CharField()
    webshop_link = serializers.CharField()

    def get_template(self):
        return '/vouchers/new_fund_created'


class ProviderApprovedEmailSerializer(BaseEmailSerializer):
    fund_name = serializers.CharField()
    provider_name = serializers.CharField()
    sponsor_name = serializers.CharField()

    def get_template(self):
        return '/vouchers/provider_approved'


class ProviderAppliedEmailSerializer(BaseEmailSerializer):
    provider_name = serializers.CharField()
    sponsor_name = serializers.CharField()
    fund_name = serializers.CharField()
    sponsor_dashboard_link = serializers.CharField()

    def get_template(self):
        return '/vouchers/provider_applied'


class NewProductAddedEmailSerializer(BaseEmailSerializer):
    sponsor_name = serializers.CharField()
    fund_name = serializers.CharField()

    def get_template(self):
        return '/vxouchers/new_product_added'


class ProviderRejectedSerializer(BaseEmailSerializer):
    provider_name = serializers.CharField()
    sponsor_name = serializers.CharField()
    fund_name = serializers.CharField()

    def get_template(self):
        return '/vouchers/provider_rejected'


class SendVoucherViaEmailSerializer(BaseEmailSerializer):
    fund_product_name = serializers.CharField()
    qr_url = serializers.CharField()

    def get_template(self):
        return '/vouchers/voucher_sended_via_email'


class SuccessPaymentSerializer(BaseEmailSerializer):
    fund_name = serializers.CharField()
    current_budget = serializers.CharField()

    def get_template(self):
        return '/vouchers/payment_success'
