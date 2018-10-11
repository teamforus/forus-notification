import django
from rest_framework import serializers


class BaseSerializer(serializers.Serializer):


    reffer_id = serializers.CharField()


    def get_template(self):
        raise NotImplementedError('Template not implimented')


    def get_lang_template(self):
        return  django.utils.translation.get_language() + self.get_template()

    def validate(self, attrs):
        self.reffer_id = attrs['reffer_id']
      #  self.data = {'username': '1111'} #attrs
        return attrs