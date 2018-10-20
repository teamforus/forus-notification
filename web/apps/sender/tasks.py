import time

from apps.core.celery import app
from apps.email_sender.email_sender import Sender as EmailSender
from apps.email_sender.fcm_sender import Sender as FcmSender
from apps.notification_user.models import User


#@app.task(bind=True)
def send_mobile_push(task, reffer_user_id, title, body):
    user = User.objects.filter(reffer_id=reffer_user_id).get()
    email_sender = FcmSender(user)
    email_sender.send_push(title, body)

@app.task(bind=True)
def send_email(task, reffer_user_id, template, data):
    user = User.objects.filter(reffer_id=reffer_user_id).get()
    email_sender = EmailSender(user)
    email_sender.send_email(template, data)
