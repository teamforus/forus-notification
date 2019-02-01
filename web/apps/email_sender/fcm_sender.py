import os

from django.conf import settings
from fcm_django.models import FCMDevice
from mail_templated import send_mail

from apps.notification_user.models import UserConnectionField, UserConnectionFCMDevice


class Sender():
    def __init__(self, user):
        self.user = user

    def send_push(self, title, body):
        connects = UserConnectionFCMDevice.objects.filter(
            user_connection = UserConnectionField.objects.find_type_connection_by_user(self.user, UserConnectionField.FIREBASE_TYPE)
        ).all()

        for connect in connects:
            if connect.device:
                connect.device.send_message(title=title, body=body)
