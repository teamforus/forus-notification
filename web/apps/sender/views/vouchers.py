from apps.sender import serializers
from apps.sender.views.api import ApiSendView


class NewFund(ApiSendView):
    serializer_class = serializers.NewFundEmailSerializer

class ForusUsersCalc(ApiSendView):
    serializer_class = serializers.ForusUsersCalcSerializer

class NewFundCreated(ApiSendView):
    serializer_class = serializers.NewFundCreatedEmailSerializer


class ProviderAppliedView(ApiSendView):
    serializer_class = serializers.ProviderAppliedEmailSerializer


class NewProductAddedView(ApiSendView):
    serializer_class = serializers.NewProductAddedEmailSerializer


class ProviderRejectedView(ApiSendView):
    serializer_class = serializers.ProviderRejectedSerializer


class SendVoucherViaEmailView(ApiSendView):
    serializer_class = serializers.SendVoucherViaEmailSerializer


class ProviderApprovedView(ApiSendView):
    serializer_class = serializers.ProviderApprovedEmailSerializer

    def get_data(self, ser):
        data = super(ProviderApprovedView, self).get_data(ser)
        # data['date_start'] = '{:%B %d, %Y}'.format(data['date_start'])
        return data


class PaymentSuccessView(ApiSendView):
    serializer_class = serializers.SuccessPaymentSerializer
