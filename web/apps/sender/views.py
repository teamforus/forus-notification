from django.conf import settings
from django.core import mail
from django.shortcuts import render

# Create your views here.
from rest_framework import generics, status
from rest_framework.response import Response

from apps.sender import serializers
from templated_email import send_templated_mail

class TestEmail(generics.GenericAPIView):

    serializer_class = serializers.SenderSerializer

    def post(self, request):
        print(settings.EMAIL_PORT)
        send_templated_mail(
            template_name='welcome',
            from_email='mk@gmail.com',
            сс=['pantyukhov.p@gmail.com'],
            bcc=['pantyukhov.p@gmail.com'],
            recipient_list=['pantyukhov.p@gmail.com'],
            context={
                'username': 'dwadawdwadwadwad',
            },
            # Optional:
            # cc=['cc@example.com'],
            # bcc=['bcc@example.com'],
            # headers={'My-Custom-Header':'Custom Value'},
            # template_prefix="my_emails/",
            # template_suffix="email",
        )
        return Response({}, status=status.HTTP_200_OK)


