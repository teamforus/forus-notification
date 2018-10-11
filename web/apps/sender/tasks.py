import time
from templated_email import send_templated_mail

from apps.core.celery import app
from apps.email_sender.sender import Sender as EmailSender
from apps.notification_user.models import User


@app.task(bind=True)
def send_email(task, user_pk, template, data):
    user = User.objects.filter(pk=user_pk).get()
    email_sender = EmailSender(user)
    email_sender.send_email(template, data)
