from rest_framework import generics, status
from rest_framework.response import Response

from apps.sender.mixin import BaseSendMixin


class ApiSendView(BaseSendMixin,generics.GenericAPIView):
    def post(self, request):
        ser = self.serializer_class(data=request.data)
        if ser.is_valid():
            attrs = ser._validated_data
            data = {}
            for rdata in attrs:
                data[rdata] = attrs[rdata]
            self.send(reffer_user_id=ser.reffer_id, template=ser.get_lang_template(), data=data)

        return Response({'ok': True}, status=status.HTTP_200_OK)
