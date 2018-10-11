from apps.sender.tasks import send_email


class BaseSendMixin(object):
    def send(self, reffer_user_id, template, data):
        send_email.delay(reffer_user_id, template, data)
        pass
