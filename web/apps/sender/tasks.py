import time

from apps.core.celery import app
from apps.email_sender.sender import Sender as EmailSender
from apps.notification_user.models import User


@app.task(bind=True)
def send_email(task, reffer_user_id, template, data):
    user = User.objects.filter(reffer_id=reffer_user_id).get()
    email_sender = EmailSender(user)
    email_sender.send_email(template, data)
