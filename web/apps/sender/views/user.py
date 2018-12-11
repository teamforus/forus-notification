from apps.sender import serializers
from apps.sender.views.api import ApiSendView


class EmailActivation(ApiSendView):
    serializer_class = serializers.EmailActivationSerializer


