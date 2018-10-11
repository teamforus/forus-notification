from django.shortcuts import render

# Create your views here.
from rest_framework import generics, status
from rest_framework.response import Response

from apps.notification_user.mixins import UserConnectionMixin
from apps.notification_user.serializers import UserConnectionFieldSerializer


class AddConnectionView(UserConnectionMixin, generics.CreateAPIView):
    serializer_class = UserConnectionFieldSerializer

    def perform_create(self, serializer):
        self.create_connection(serializer.user_id, serializer.type, serializer.value)
