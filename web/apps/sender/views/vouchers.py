from apps.sender import serializers
from apps.sender.views.api import ApiSendView


class NewFund(ApiSendView):
    serializer_class = serializers.NewFundSerializer


class ProviderAppliedView(ApiSendView):
    serializer_class = serializers.ProviderAppliedSerializer


class ProviderApprovedView(ApiSendView):
    serializer_class = serializers.ProviderApprovedSerializer

    def get_data(self, ser):
        data = super(ProviderApprovedView, self).get_data(ser)
        data['date_start'] = '{:%B %d, %Y}'.format(data['date_start'])
        return data
