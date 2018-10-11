from rest_framework import serializers


class BaseSerializer(serializers.Serializer):
    reffer_id = serializers.CharField()



    def validate(self, attrs):
        self.reffer_id = attrs['reffer_id']
      #  self.data = {'username': '1111'} #attrs
        return attrs