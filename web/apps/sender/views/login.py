from apps.sender import serializers
from apps.sender.views.api import ApiSendView


class LoginViaEmail(ApiSendView):
    serializer_class = serializers.LoginViaEmailSerializer