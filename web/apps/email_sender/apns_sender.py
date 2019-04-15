import os

from apns2.client import APNsClient
from apns2.payload import Payload, PayloadAlert
from django.conf import settings
from fcm_django.models import FCMDevice
from mail_templated import send_mail

from apps.notification_user.models import UserConnectionField, UserConnectionFCMDevice


class Sender():
    def __init__(self, user):
        self.user = user

    def send_push(self, title, body):
        connects = UserConnectionField.objects.find_type_connection_by_user(self.user, UserConnectionField.APNS_TYPE)

        client = APNsClient(settings.APNS_KEY_LOCATION, use_sandbox=settings.APNS_SENDBOX, use_alternative_port=False)

        payload = Payload(alert=PayloadAlert(title=title, body=body), sound="default", badge=1)
        for connect in connects:
            client.send_notification(token_hex=connect.value, notification=payload, topic=settings.APNS_BUNDLE_ID)
