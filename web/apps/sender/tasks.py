import time

from django.conf import settings
from twilio.rest import Client

from apps.core.celery import app
from apps.email_sender.email_sender import Sender as EmailSender
from apps.email_sender.fcm_sender import Sender as FcmSender
from apps.email_sender.apns_sender import Sender as ApnsSender
from apps.notification_user.models import User


# @app.task(bind=True)
def send_mobile_sms(self, phone, body):
    from twilio.rest import Client

    account_sid = settings.TWILIO_ACCOUNT_SID
    auth_token = settings.TWILIO_AUTH_TOKEN
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_=settings.TWILIO_PHONE_NUMBER,
        body=body,
        to=phone
    )

    print(message.sid)
    # client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    # message = client.messages.create(to='+79215669603', from_='+3197014200722',
    #                                  body=body)


@app.task(bind=True)
def send_mobile_push(self, reffer_user_id, title, body):
    user = User.objects.filter(reffer_id=reffer_user_id).get()

    email_sender = FcmSender(user)
    email_sender.send_push(title, body)


    apns_sender = ApnsSender(user)
    apns_sender.send_push(title, body)


@app.task(bind=True)
def send_email(self, reffer_user_id, email, template, data):
    print(reffer_user_id)
    if reffer_user_id:
        user = User.objects.filter(reffer_id=reffer_user_id).get()
    else:
        user = None
    email_sender = EmailSender(user, email)
    email_sender.send_email(template, data)
