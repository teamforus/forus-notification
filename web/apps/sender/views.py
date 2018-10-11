from django.conf import settings
from django.core import mail
from django.shortcuts import render

# Create your views here.
from rest_framework import generics, status
from rest_framework.response import Response

from apps.sender import serializers
from templated_email import send_templated_mail

from apps.sender.tasks import send_email


class TestEmail(generics.GenericAPIView):

    serializer_class = serializers.SenderSerializer

    def post(self, request):
        send_email.delay(request.reffer_user.pk)

        return Response({}, status=status.HTTP_200_OK)


