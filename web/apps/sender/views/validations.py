from apps.sender import serializers
from apps.sender.views.api import ApiSendView


class SponsorAddYouAsValidatorApi(ApiSendView):
    serializer_class = serializers.SponsorAddYouAsValidatorEmailSerializer



class NewValidationRequestApi(ApiSendView):
    serializer_class = serializers.NewValidationRequestEmailSerializer



