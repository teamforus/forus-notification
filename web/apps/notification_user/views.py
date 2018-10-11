from django.shortcuts import render

# Create your views here.
from rest_framework import generics, status
from rest_framework.response import Response

from apps.notification_user.serializers import UserConnectionFieldSerializer


class AddConnectionView(generics.CreateAPIView):
    serializer_class = UserConnectionFieldSerializer

    def perform_create(self, serializer):
        pass
