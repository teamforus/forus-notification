import os

from django.conf import settings
from django.core.mail import get_connection
from mail_templated import send_mail

from apps.notification_user.models import UserConnectionField


class Sender():
    def __init__(self, user):
        self.user = user
        self.backend_index = 0

    def send_email(self, template, data):
        connections = UserConnectionField.objects.find_emails_connection_by_user(self.user)

        for connection in connections:
            email = connection.value
            self.send_email_with_connection(template, data, email)

    def send_email_with_connection(self, template, data, email):

        for iteration in range(10):
            try:
                print(settings.EMAIL_CONNACTIONS)
                smtp_connection = get_connection(
                    host=settings.EMAIL_CONNACTIONS[iteration].get('EMAIL_HOST'),
                    port=settings.EMAIL_CONNACTIONS[iteration].get('EMAIL_PORT'),
                    username=settings.EMAIL_CONNACTIONS[iteration].get('EMAIL_HOST_USER'),
                    password=settings.EMAIL_CONNACTIONS[iteration].get('EMAIL_HOST_PASSWORD'),
                    use_tls=settings.EMAIL_CONNACTIONS[iteration].get('EMAIL_USE_TLS'),
                    use_ssl=settings.EMAIL_CONNACTIONS[iteration].get('EMAIL_USE_SSL'),
                )
                send_mail(template, data, settings.EMAIL_CONNACTIONS[iteration].get('EMAIL_FROM'), [email], connection=smtp_connection)
                break
            except:
                pass
