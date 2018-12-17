from apps.sender import serializers
from apps.sender.views.api import ApiSendView


class NewFund(ApiSendView):
    serializer_class = serializers.NewFundEmailSerializer

class ForusUsersCalc(ApiSendView):
    serializer_class = serializers.ForusUsersCalcSerializer

class ProductBought(ApiSendView):
    serializer_class = serializers.ProductBoughtSerializer

class ProductSoldout(ApiSendView):
    serializer_class = serializers.ProductSoldoutSerializer

class NewFundCreated(ApiSendView):
    serializer_class = serializers.NewFundCreatedEmailSerializer

class ForusNewFundCreated(ApiSendView):
    serializer_class = serializers.ForusNewFundCreatedEmailSerializer

class ProviderAppliedView(ApiSendView):
    serializer_class = serializers.ProviderAppliedEmailSerializer


class NewProductAddedView(ApiSendView):
    serializer_class = serializers.NewProductAddedEmailSerializer


class ProviderRejectedView(ApiSendView):
    serializer_class = serializers.ProviderRejectedSerializer

class ShareProductView(ApiSendView):
    serializer_class = serializers.ShareProductSerializer

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
