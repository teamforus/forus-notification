from apps.sender.tasks import send_email, send_mobile_push, send_mobile_sms


class BaseSendMixin(object):
    def send_push(self, reffer_user_id, title, body):
        send_mobile_push.delay(reffer_user_id, title, body)

    def send_sms(self, phone, title):
        send_mobile_sms(self, phone, title)

    def send(self, reffer_user_id, template, data):
        send_email.delay(reffer_user_id, template, data)
        pass


