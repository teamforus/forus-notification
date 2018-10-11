import django

from apps.notification_user.models import User


class SenderMiddleWare(django.utils.deprecation.MiddlewareMixin):
    def process_request(self, request):
        reffer_id = request.GET.get('reffer_id')
        if reffer_id:
            user = User.objects.filter(reffer_id=reffer_id).get()
            request.reffer_user = user