import time
from templated_email import send_templated_mail

from apps.core.celery import app
from apps.email_sender.sender import Sender
from apps.notification_user.models import User


@app.task(bind=True)
def send_email(task, user_pk):
    user = User.objects.filter(pk=user_pk).get()
    sender = Sender(user)
    sender.send_email('welcome', {'username': 'dawdwadwadwaaw'})
