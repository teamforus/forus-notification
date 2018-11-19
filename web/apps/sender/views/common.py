
from rest_framework import generics, status
from rest_framework.response import Response

from apps.sender.mixin import BaseSendMixin
from apps.sender.views import ApiSendView, serializers


class PushNotificationView(BaseSendMixin, generics.GenericAPIView):
    serializer_class = serializers.PushNotificationSerializer

    def post(self, request):
        ser = self.serializer_class(data=request.data)
        if ser.is_valid():
            self.send_push(ser.reffer_id, ser.title, ser.body)
            return Response({'ok': True}, status=status.HTTP_200_OK)
        else:
            return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)


class SmsNotificationView(BaseSendMixin, generics.GenericAPIView):
    serializer_class = serializers.SmsNotificationSerializer

    def post(self, request):
        ser = self.serializer_class(data=request.data)
        if ser.is_valid():
            self.send_sms( ser.phone, ser.title)
            return Response({'ok': True}, status=status.HTTP_200_OK)
        else:
            return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

