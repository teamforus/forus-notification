from apps.sender import serializers
from apps.sender.views.api import ApiSendView


class NewFund(ApiSendView):
    serializer_class = serializers.NewFundSerializer



